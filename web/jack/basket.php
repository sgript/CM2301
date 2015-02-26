<?php
	include 'cookie.php';
?>
<!DOCTYPE html >
<html lang="en">
	<head>
		<title>Shopnet - Basket</title>
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
					<?php
					$tot = 0;
					if (mysqli_num_rows($mysqli->query($basketresult)) > 0){
						$basketprint = $mysqli->query($basketresult) or die($mysqli->error.__LINE__);
						echo "<table>";
						echo "<thead><th></th><th>Product</th><th id='Price'>Price</th><th>Quantity</th><th></th></thead>";
						while ($basketr = mysqli_fetch_assoc($basketprint)){
							$bprod = "SELECT ProductID,Manufacturer,Name,Brief,Price * Offers as newprice,Image FROM Products WHERE ProductID = " . $basketr['ProductID'] . ""; // Selecting all of the products in the basket of the current user
							$pre = $mysqli->query($bprod);

							while ($btab = mysqli_fetch_assoc($pre)){
								echo "<tbody>
								<tr>
								<td rowspan='2'><img id='product' src='images/" . $btab['Image'] . "' height=105/></td>
								<td id='ptitle'><a href=product.php?id=" . $btab['ProductID'] . ">" . $btab['Manufacturer'] . " " . $btab['Name'] . "</td>
								<td id=Price>&pound;". number_format(floatval($btab['newprice']),2,".",",") . "</td>
								<td><form method='post' action='update.php?id=" . $btab['ProductID'] . "' id='quant'><input type='text' id='qno' name='qno' value='" . $basketr['Quantity'] . "'/></td>
								</tr>
								<tr>
								<td id='brief'>" . $btab['Brief'] . "</td>
								<td><a href='rembasket.php?id=" . $btab['ProductID'] . "''><img src='images/delbasket.png' width=50px/></a></td>
								<td><input type='submit' name='submit' value='Update quantity'/></form>
								</tr>
								</tbody>";//table format, including a quantity form and submission
								$tot = $tot + ($basketr['Quantity'] * $btab['newprice']);//Total price 
							}
						}
						echo "<tfoot>
						<tr>
						<td><a href='delall.php'><img src='images/delall.png' width=50px/></a></td>
						<td>Total price:</td>
						<td>&pound;" . number_format(floatval($tot),2,".",",") . "</td>
						<td><a href='paynow.php'>Checkout</a></td>
						</tr>
						</tfoot>";
					}
					else {
								echo "<tbody>You have no items in your basket.</tbody>";//if no items in basket display this
					}
					if(isset($_GET['fb'])){
						$feed = $_GET['fb'];
						if($feed == 'del'){
							echo "<p>Item successfully removed from basket!</p>";
						} elseif($feed == 'upd'){
							echo "<p>Item quantity successfully updated!</p>";
						} elseif ($feed == 'pay') {
							echo "<p>Your transaction was successful!</p>";
						} elseif ($feed == 'nolog'){
							echo "<p>You must register with us to do that!</p>";
						}
					}
					?>
					</table>
			</div>
		</div>
	</body>
</html>
