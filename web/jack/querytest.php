<?php
	$connect = mysqli_connect("ephesus.cs.cf.ac.uk","c1327650","berlin","c1327650");
	if(isset($_COOKIE["shopnet_login"])){
		$UserID = $_COOKIE['shopnet_login'];
		$basketresult = mysqli_query($connect, "SELECT * FROM Basket WHERE UserID='".$_COOKIE['shopnet_login']."'");
	}
	elseif(isset($_COOKIE["shopnet"])){
		$basketresult = mysqli_query($connect, "SELECT * FROM Basket WHERE UserID='".$_COOKIE['shopnet']."'");
		$UserID = $_COOKIE['shopnet'];
	}
	else{
		$UserID = uniqid("",true);
		setcookie("shopnet",$UserID,time()+1800,'/');	
	}
	$basket = array();
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
				<a href="Home.php"><img src="Banner.png" id="Top" alt="Shopnet Home" width=300 Title="Shopnet Home" /></a>
				<form method="post" action="query.php" id='mainQuery'>
					<input type="text" name="searchTerm" placeholder="Search for a product..."/>
					<select name="category">
					<?php
					$DB_NAME = 'c1327650';
					$DB_HOST = 'ephesus.cs.cf.ac.uk';
					$DB_USER = 'c1327650';
					$DB_PASS = 'berlin';
					$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
					$dquery = "SELECT DISTINCT Category FROM Products";
					$dresult = $mysqli->query($dquery) or die($mysqli->error.__LINE__); 
					echo "<option value='*' selected>All categories</option>";
					while ($dropdown = mysqli_fetch_assoc($dresult)){
						$drop = implode($dropdown);
						echo "<option value=" . urlencode($drop) .">" . $drop . "</option>";
						$subq = "SELECT DISTINCT Subcategory FROM Products WHERE Category='$drop'";
						$subr = $mysqli->query($subq) or die($mysqli->error.__LINE__);
						while ($Subc = mysqli_fetch_assoc($subr)){
							$Subd = implode($Subc);
							echo "<option value=" . urlencode($Subd) . ">|--" . $Subd . "</option>";
						}
					}
					?>
					<input type="submit" name="submit" value="Go!"/>
				</form>
			</header>
		</h1>	
		<div id="wrapper">
		<nav id="navigation">
			<h2>
				Categories
			</h2>
			<ul>
				<?php
					$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
					$query = "SELECT DISTINCT Category FROM Products";
					$result = $mysqli->query($query) or die($mysqli->error.__LINE__); 
					while ($Category = mysqli_fetch_assoc($result)){
						$Cat = implode($Category);
						echo "<li><a href=query.php?cat=" . $Cat .">" . $Cat . "</a></li>";
						$subquery = "SELECT DISTINCT Subcategory FROM Products WHERE Category='$Cat'";
						$subresult = $mysqli->query($subquery) or die($mysqli->error.__LINE__);
						$i = 0;
						echo "<ul>";
						while ($Subcategory = mysqli_fetch_assoc($subresult)){
							$Sub = implode($Subcategory);
							echo "<li><a href=query.php?cat=" . urlencode($Sub) . ">" . $Sub . "</a></li>";
						} echo "</ul>";
					}
				?>
			</ul>
		</nav>
		<div id="rightcol">
			<?php		
				$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
				$dbquery = "SELECT Firstname FROM Users WHERE UserID='$UserID'";
				$IDresult = $mysqli->query($dbquery) or die($mysqli->error.__LINE__);
				$count = mysqli_num_rows($IDresult);
				$Names = mysqli_fetch_assoc($IDresult);
				echo $UserID;
				if ($count != 0){
					$Name = implode($Names);
					echo "Welcome back, " . $Name . ". Not " . $Name . "? <a href='logout.php'>Sign in as a different user or log out.</a>";
				} else {
					echo "<form method='post' action='login.php'>";	
					echo 	"Email address: <input type='text' name='email' placeholder='Email address' /><br/>";
					echo 	"Password: <input type='password' name='password' placeholder='Password'/><br/>";
					echo 	"<input type='submit' name='submit' value='Login'/>";
					echo 	"</form>";
					echo "<p>Not a member? <a href='register.php'>Register now!</a></p>";
				}
			?>
		</div>
		<div id="Centre">
			<h2>
				<table>
					<th></th><th>Product</th><th id="Price">Price</th>
					<?php
						$qcat = $_GET['cat'];
						$pcat = $_POST['category'];		
						$search = $_POST['searchTerm'];
						if ($pcat != ''){
							$categoryq = "SELECT Name,Price,Price * Offers AS newprice, Manufacturer,ProductID,Image,Brief FROM Products WHERE (Name LIKE '$search' OR Brief LIKE '$search' OR Description LIKE '$search' OR Manufacturer LIKE '$search') AND (Category='$pcat' OR Subcategory='$pcat')";
						} else {
						$categoryq = "SELECT Name,Price,Price * Offers As newprice, Manufacturer,ProductID,Image,Brief FROM Products WHERE (Category='$qcat' OR Subcategory='$qcat')";
						}
						$qresult = $mysqli->query($categoryq) or die($mysqli->error.__LINE__);
						while ($qtab = mysqli_fetch_assoc($qresult)){
							if (empty($qresult) == False){
								echo "<tr><td rowspan='2'><img id='product' src='images/" . $qtab['Image'] . "' height=105/></td><td id='ptitle'><a href=product.php?id=" . $qtab['ProductID'] . ">" . $qtab['Manufacturer'] . " " . $qtab['Name'] . "</td><td id=Price>&pound;". number_format(floatval($qtab['newprice']),2,".",",") . "</td></tr><tr><td id='brief'>" . $qtab['Brief'] . "</td><td><a href='basketadd.php'><img src=add2basket.png/></a></td></tr>";
							} else {
								echo "Sorry, no results for search '" . $search . "'. Try another search term?";
							}
						}
					?>
				</table>
			</h2>
		</div>
		</div>
	</body>
</html>
