<?php
	include 'cookie.php';
?>
<!DOCTYPE html >
<html lang="en">
	<head>
		<title>Shopnet - Product view</title>
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
					$id = $_GET['id'];
					$getidinfo = "SELECT Name,Price,Price * Offers As newprice,Manufacturer,ProductID,Image,Description FROM Products WHERE ProductID='$id'";//fetch details of product and display in a table with a buy now button
					$getresult = $mysqli->query($getidinfo) or die($mysqli->error.__LINE__);					
					$idresult = mysqli_fetch_assoc($getresult);
					if ($idresult['newprice'] != $idresult['Price']){
						echo "<p id='pr'>Was: &pound;" . $idresult['Price'] . "<br/> Now: &pound;" . number_format(floatval($idresult['newprice']),2,".",",") . "!</p>";
					} else {
						echo "<p id='pr'>&pound;" . number_format(floatval($idresult['Price']),2,".",",") . "</p>";
					}
					echo "<a id='add' href='addbasket.php?id=" . $idresult['ProductID'] . "''><img src='images/blackadd.png' width=50px/></a>";
					echo "<h3 id=prodtitle>" . $idresult['Manufacturer'] . " " . $idresult['Name'] . "</h3>";
					echo "<img src='images/" . $idresult['Image'] . "' width=400px id='prodimg'/>";
					echo "<p id='desc'>" . $idresult['Description'] . "</p>";
				?>
			</h2>
		</div>
		</div>
	</body>
</html>

