<?php
	include 'cookie.php';
?>
<!DOCTYPE html >
<html lang="en">
	<head>
		<title>Shopnet - Home</title>
		<meta charset="utf-8" />
		<link rel="stylesheet" type="text/css" href="Home.css">
	</head>
	<body>
		<h1>
			<header>
				<?php
					include 'header.php';
				?>
			</header>
		</h1>	
		<div id="wrapper">
		<?php
			include 'cat.php';
		?>
		<div id="rightcol">
			<?php		
				include 'loginform.php';
			?>
		</div>
		<div id="Centre">
			<h2>

					<?php
						if (isset ($_GET['cat'])){
							$pcat = $_GET['cat'];
						} 
						if (isset($_POST['searchTerm'])){
							$search = $_POST['searchTerm'];
						}
						if (isset($_POST['category'])){
							$pcat = $_POST['category'];
						}
						if ((isset($pcat)) and ($pcat == '.') and (isset($_POST['searchTerm']))){
							$categoryq = "SELECT Name,Price,Price * Offers AS newprice, Manufacturer,ProductID,Image,Brief FROM Products WHERE (Name LIKE '%$search%' OR Brief LIKE '%$search%' OR Description LIKE '%$search%' OR Manufacturer LIKE '%$search%') AND (Category REGEXP '$pcat' OR Subcategory REGEXP '$pcat')";
						} elseif ((isset($_POST['category'])) and (isset($_POST['searchTerm']))){
							$categoryq = "SELECT Name,Price,Price * Offers AS newprice, Manufacturer,ProductID,Image,Brief FROM Products WHERE (Name LIKE '%$search%' OR Brief LIKE '%$search%' OR Description LIKE '%$search%' OR Manufacturer LIKE '%$search%') AND (Category = '$pcat' OR Subcategory = '$pcat')";
						} elseif ((isset($_GET['cat']))) {
							$categoryq = "SELECT Name,Price,Price * Offers As newprice, Manufacturer,ProductID,Image,Brief FROM Products WHERE (Category='$pcat' OR subcategory='$pcat')";
						} else {
							$categoryq = "SELECT Name,Price,Price * Offers As newprice, Manufacturer, ProductID,Image,Brief FROM Products WHERE Category REGEXP '.' ";
						}
						if (isset($_GET['sort'])){
							$categoryq = $categoryq . "ORDER BY " . $_GET['sort'];
						}
						$qresult = $mysqli->query($categoryq) or die($mysqli->error.__LINE__);
						include 'sort.php';
						while ($qtab = mysqli_fetch_assoc($qresult)){//displaying results in a table
							if (mysqli_num_rows($qresult) > 0){
								echo "<tbody>
								<tr>
								<td rowspan='2'><img id='product' src='images/" . $qtab['Image'] . "' height=105/></td>
								<td id='ptitle'><a href=product.php?id=" . $qtab['ProductID'] . ">" . $qtab['Manufacturer'] . " " . $qtab['Name'] . "</td>
								<td id=Price>&pound;". number_format(floatval($qtab['newprice']),2,".",",") . "</td>
								</tr>
								<tr>
								<td id='brief'>" . $qtab['Brief'] . "</td>
								<td><a href='addbasket.php?id=" . $qtab['ProductID'] . "''><img src='images/blackadd.png' width=50px/></a></td>
								</tr>
								</tbody>";
							}
						}
					?>
				</table>
			</h2>
		</div>
		</div>
	</body>
</html>
