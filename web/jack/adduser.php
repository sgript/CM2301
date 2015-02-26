<!DOCTYPE html >
	<html lang="en">
	<head>
		<title>Shopnet - Register - redir</title>
		<meta charset="utf-8" />
	</head>
	<body>
		<?php //fetches all form data from previous page
			$connect = mysqli_connect("ephesus.cs.cf.ac.uk","c1327650","berlin","c1327650");
			$firstname = strip_tags(mysqli_real_escape_string($connect,trim($_POST['first'])));
			$lastname = strip_tags(mysqli_real_escape_string($connect,trim($_POST['last'])));
			$email = strip_tags(mysqli_real_escape_string($connect,trim($_POST['email'])));
			$pass = password_hash($_POST['password'],PASSWORD_BCRYPT);
			$AL1 = strip_tags(mysqli_real_escape_string($connect,trim($_POST['address1'])));
			$AL2 = strip_tags(mysqli_real_escape_string($connect,trim($_POST['address2'])));
			$AL3 = strip_tags(mysqli_real_escape_string($connect,trim($_POST['address3'])));
			$phone = strip_tags(mysqli_real_escape_string($connect,trim($_POST['phone'])));
			$UID = $_COOKIE["shopnet"];
			$DBNAME = 'c1327650';//information for connection to server
			$DBHOST = 'ephesus.cs.cf.ac.uk';
			$DBUSER = 'c1327650';
			$DBPASS = 'berlin';
			$mysqli = new mysqli($DBHOST, $DBUSER, $DBPASS, $DBNAME);
			if (mysqli_connect_errno()) {
				printf("Failed: %s\n", mysqli_connect_error());
				exit();
			}
			if (mysqli_num_rows($mysqli->query("SELECT * FROM Users WHERE Email='$email'"))==1){ //if this address is in the database, redirect the user
				echo "That E-mail address is already registered. Please try again with a different E-mail address.";//javascript redirection
				echo "<script type='text/javascript'>
					<!--
					document.location='Home.php';
					-->
				    </script>";
			}
			else {
			$newuser = "INSERT INTO Users(Firstname, Lastname, Password, Email, Address1, Address2, Address3, Phone, UserID) VALUES ('" . $firstname . "','" . $lastname . "','" . $pass . "','" . $email . "','" . $AL1 . "','" . $AL2 . "','" . $AL3 . "','" . $phone . "','" . $UID . "')";
			if(!$mysqli->query($newuser)){
				echo "We're sorry, your registration failed. Please contact support quoting this error number: " . $mysqli->errno . "." . $mysqli->error;//if something goes wrong print this
			} else {
				echo "Successfully registered! Please wait and you will be redirected. If you are not redirected shortly, please click the link below.";//javascript redirection
				echo "<script type='text/javascript'>
					document.location='Home.php';
				    </script>";
			}
			}
			mysqli_close($mysqli);
		?>
		</script>
	</body>
</html>
