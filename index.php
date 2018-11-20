<!DOCTYPE html>
<html>
<?php
session_start();

$l = $_POST["login"];
$p = $_POST["password"];
$h = hash("sha256",$p);




for($i = 0; $i < 100; ++$i)
{
	$e = "eleve" . (string)$i;
	if($l == $e)
	{
		$l = "pass/" . $e . ".txt";
		$f = fopen($l, "r");
		$H = fread($f,filesize($l));
		fclose($f);
		if($h == $H)
		{
			$_SESSION["eleve"] = $i;
			header("Location: notes.php");
			die();
		}
	}
}



?>




    <head>
		<link rel="shortcut icon" type="image/png" href="img/logo.png"/>
		<link rel="stylesheet" type="text/css" href="index.css">
		<meta http-equiv= "content-type" content= "text/html; charset=UTF-8" >
        <title> Institut Villebon Charpak </title>
        <script src="index.js"></script>
    </head>

    <body background="img/bg.jpg">
        <div class="title">
			<br>
            <form class="" action="index.php" method="post">
                Login :
                <input type="text" name="login">
                <br>
                Password :
                <input type="password" name="password">
				<br>
				<input type="submit" value="Se connecter">
            </form>
			<?php echo $l . " / " . $p . " / " . $h ?>
        </div>
    </body>
</html>
