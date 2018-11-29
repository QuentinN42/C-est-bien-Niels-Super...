<!DOCTYPE html>
<html>
<?php
$s = "Data/Settings/";
$p = "Data/Prof/";
$lmod = $s . "modele.txt";
$lnbrcontroles = $s . "nbrcontroles.txt";



function read($l){
    $f = fopen($l, "r");
    $tmp = fread($f,filesize($l));
    fclose($f);
    return $tmp;
}

function changemod($mod)
{
    $fp = fopen("Data/Settings/modele.txt", 'w');
    fwrite($fp, $mod);
    fclose($fp);
}

function changecontroles($n)
{
    $fp = fopen("Data/Settings/nbrcontroles.txt", 'w');
    fwrite($fp, $n);
    fclose($fp);
}

if(isset($_POST["mod"]))
{
    changemod($_POST["mod"]);
}
if(isset($_POST["ctrls"]))
{
    changecontroles($_POST["ctrls"]);
}



$mod = read($lmod);

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
                    Bonjour Maître
                </center>
            </h1>
            <div class="block">
                <h2>Plot des thèmes</h2>
                    Plot des XPs en fonction des thèmes :<br>
                    <img src=<?php echo $p."repartXP.png" ?>>
                    <br><br>
                <h2>Plot 4D</h2>
                    Plot des XPs en fonction des XPs en fonction des XPs en fonction des XPs :<br>
                    <img src=<?php echo $p."3D.png" ?>>
                    <br><br>
                <h2>Modeles</h2>
                    <h3>Modele linéaire</h3>
                    <img src=<?php echo $lin."png" ?>>
                    <br>
                    <?php echo read($lin."txt") ?>
                    <br><br>

                    <h3>Modele logarithmique</h3>
                    <img src=<?php echo $log."png" ?>>
                    <br>
                    <?php echo read($log."txt") ?>
                    <br><br>

                    <h3>Modele inverse</h3>
                    <img src=<?php echo $inv."png" ?>>
                    <br>
                    <?php echo read($inv."txt") ?>
                    <br><br>

                    <h3>Modele racine carré</h3>
                    <img src=<?php echo $car."png" ?>>
                    <br>
                    <?php echo read($car."txt") ?>
                    <br><br>
                <h2>Changement de modèle</h2>
                    <form action="prof.php" method="post">
                        <input  type="radio" name="mod" value="lin"> Linéaire </button><br>
                        <input  type="radio" name="mod" value="log" checked> Logarithmique </button><br>
                        <input  type="radio" name="mod" value="inv"> Inverse </button><br>
                        <input  type="radio" name="mod" value="car"> Racine carré </button><br>
                        <button type="submit" name="button"> Valider </button>
                    </form>
                    <form action="prof.php" method="post">
                        <input  type="number" name="ctrls" value="0"><br>
                        <button type="submit" name="button"> Valider </button>
                    </form>
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
