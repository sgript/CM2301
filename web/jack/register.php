<?php
	include 'cookie.php';
?>
<!DOCTYPE html >
<html lang="en">
	<head>
		<title>Shopnet - Register</title>
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
		</div>
		<div id="Centre">
			<h2>
				Create an account
			</h2>

			<form method="post" action="adduser.php" name="reg">
				First name: <input type="pattern='^[A-Z][-a-z0{3,}'" name="first" placeholder="First name" required/><sup>*</sup><br/>
				Last name: <input type="pattern='^[A-Z][-a-zA-Z]+$'" name="last" placeholder="Last name" required/><sup>*</sup><br/>
				Email address: <input type="email" name="email" placeholder="Email address" required/><sup>*</sup><br/>
				Confirm Email address: <input type="email" name="email1" placeholder="Email address" required/><sup>*</sup><br/>
				Password: <input type="password" name="password" placeholder="Password" required/><sup>*</sup><br/>
				Confirm password: <input type="password" name="password1" placeholder="Password" required/><sup>*</sup><br/>
				Address Line 1: <input type="pattern" name="address1" placeholder="Address Line 1" required/><sup>*</sup><br/>
				Address Line 2: <input type="pattern" name="address2" placeholder="Address Line 2" required/><sup>*</sup><br/>
				Address Line 3: <input type="pattern=''" name="address3" placeholder="Address Line 3" required/><sup>*</sup><br/>
				Phone number: <input type="text" name="phone" placeholder="Phone number"/><br/>
				<input type="submit" name="submit" value="Register"/>
			</form>
			<p>A '*' denotes a required field.</p>
		</div>
	</div>
</html>

