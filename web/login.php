<?php
	error_reporting (E_ALL ^ E_NOTICE);
	
	$con = mysqli_connect("ephesus.cs.cf.ac.uk","c1312433","berlin","c1312433");
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}
	else
		echo "<center><img src='faceten.gif' alt='faceten'></center>";

	session_start(); 
?>

<!DOCTYPE HTML>

<html>
<head>
	<title> Login </title>
	<script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
	<link type="text/css" rel="stylesheet" href="css/bootstrap.css"/>
	<link href="signin.css" rel="stylesheet">
</head>
<body>

<div class="container">

<?php
  $form = "<form class='form-signin' action='./login.php' method='POST'>


    <h2 class='form-signin-heading'>Username:</h2>
    <input type='text' name='user' class='form-control' placeholder='Username' autofocus>
    <h2 class='form-signin-heading2'>Password:</h2>
    <input type='password' name='password' class='form-control' placeholder='Password'>
    <button class='btn btn-lg btn-primary btn-block' type='submit' name='loginbtn' value='Login'> Login</button>
  </form>
 
</div> <!-- /container -->
<script src='js/bootstrap.js'></script>";

// zz
	if ($_POST['loginbtn']){
		$user = $_POST['user'];
		$password = $_POST['password'];

		if ($user) {
			if ($password) {
				require("connect.php");
				$password = md5(md5("ihefbFEW".$password."Q0i03r2r3"));
				// echo $password;

				$query = mysqli_query($con, "SELECT * FROM administrators WHERE username = '$user'");

				$numrows = mysqli_num_rows($query);

				if ($numrows == 1) {
					$row = mysqli_fetch_assoc($query);
					$dbid = $row['id'];
					$dbuser = $row['username'];
					$dbpass = $row['password'];
					$dbactive = $row['active'];

					if ($password == $dbpass) {
						if ($dbactive == 1) {
							$_SESSION['userid'] = $dbid;
							$_SESSION['username'] = $dbuser;


							echo "<center>You have been logged in as <b>$dbuser</b> <a href ='template.php'>Click here</a> to go to the admin panel.</center>";
						}
						else
							echo "<center><p class='error'>* You must activate your account to login.</center> $form";
					}
					else
						echo "<center><p class='error'>* You did not enter the correct password.</center> $form";

				}
				else
					echo "<center><p class='error'>* The username you entered was not found.</center> $form";


				mysqli_close($con);
			}
		 	else
		 		echo "<center><p class='error'>* You must enter your password.</center> $form";
		}
		else 
			echo "<center><p class='error'>* You must enter your username.</p></center> $form";
	}
	else
			echo $form;
?> 
</body>
</html>












