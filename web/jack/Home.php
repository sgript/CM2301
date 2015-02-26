<?php
	include 'cookie.php'; //Admin, add quantity, hide side panels, form validation
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
					Current offers
					<?php
						$offers = "SELECT Name,Price,Price * Offers AS newprice,Manufacturer,Image,ProductID,Brief FROM Products WHERE Offers != 1";
						$qresult = $mysqli->query($offers) or die($mysqli->error.__LINE__);
						include 'sort.php';
						while ($otab = mysqli_fetch_assoc($qresult)){
							echo "<tbody><tr><td rowspan='2'><img id='product' src='images/" . $otab['Image'] . "' height=105/></td><td id='ptitle'><a href=product.php?id=" . $otab['ProductID'] . ">" . $otab['Manufacturer'] . " " . $otab['Name'] . "</td><td id=Price>&pound;". number_format(floatval($otab['newprice']),2,".",",") . "</td></tr><tr class='p'><td id='brief'>" . $otab['Brief'] . "</td><td><a href='addbasket.php?id=" . $otab['ProductID'] . "'><img src='images/blackadd.png' width=50px/></a></td></tr></tbody>";
						}
					?>
					</table>
				</h2>
			</div>
		</div>
	</body>
</html>
