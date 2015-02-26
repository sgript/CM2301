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

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Template</title>
 
    <link type="text/css" rel="stylesheet" href="css/bootstrap.css"/>

    <link href="template.css" rel="stylesheet">

    <script src="error.js"></script>

  </head>

  <body>

     

    <div class="container">

    <?php 
    session_start();
    if (isset($_SESSION['username'])) {
       session_destroy();
       echo "You are logged out successfully!";
    } 
       echo "<a href='login.php' class = link2>Log Out</a>";
     ?>
      <div class="masthead">
        <nav>
          <ul class="nav nav-justified">
            <li><a href="#">Manage Users</a></li>
            <li><a href="livefeed.html">Live Feed</a></li>
            <li class="active"><a href="manageusergroups.html">Manage User Groups</a></li>
          </ul>
        </nav>

        
      </div>
    </div>

     
  </body>
</html>