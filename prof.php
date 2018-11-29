<!DOCTYPE html>
<html>
<?php
$s = "Data/Settings/";
$p = "Data/Prof/";
$lmod = $s . "modele.txt";
$lnbrcontroles = $s . "nbrcontroles.txt";


$fmod = fopen($lmod, "r");
$mod = fread($fmod,filesize($lmod));
fclose($fmod);

$lin = $p . "Modele_Lineaire.";
$inv = $p . "Modele_Inverse.";
$log = $p . "Modele_Log.";
$car = $p . "Modele_racine_carre.";



?>

    <head>
		<link rel="shortcut icon" type="image/png" href="img/logo.png"/>
		<link rel="stylesheet" type="text/css" href="prof.css">
		<meta http-equiv= "content-type" content= "text/html; charset=utf-8" >
        <title> Institut Villebon Charpak </title>
        <script src="prof.js"></script>
    </head>

    <body onresize="changeHeight()" onload="changeHeight()" onscroll="hidemain()">


        <div class="content" id="content">
            <h1 class="titre">
                <center>
                    Bonjour Maitre
                </center>
            </h1>
            <div class="block">
                <h3>Modeles</h3>
                    <h6>Modele linéaire</h6>
                    <img src=<?php echo $lin."png" ?>>
                    <?php  ?>
            </div>
        </div>
        <div class="main" id="main">
            <img class="bg" src="img/bg.jpg" alt="Institut Villebon Charpak">
                <div class="title">
                    <h1>
                        Institut Villebon Charpak
                    </h1>
                    <h2>
                        Page proffesseur
                    </h2>
                </div>
        </div>
                <br>
    </body>
</html>
