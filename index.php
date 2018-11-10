<!DOCTYPE html>
<html>
<?php
if(isset($_GET["n"]))
{
    $n = $_GET["n"];
}
else
{
    $n = 0;
}
$l = "Data/" . $n;
$s = "Data/Settings/";
$lmod = $s . "modele.txt";


$lnom   = $l . "/prenom.txt";


$lxps   = $l . "/xp";
$lxp1 = $lxp1 . "1.txt";
$lxp2 = $lxp2 . "2.txt";
$lxp3 = $lxp3 . "3.txt";
$lxp4 = $lxp4 . "4.txt";


$lnotelin = $l . "/note.txt";
$lnotelog = $l . "/notel.txt";
$lnoteinv = $l . "/notei.txt";
$lnotecar = $l . "/notec.txt";



// note lin :
$fnotelin = fopen($lnotelin, "r");
$notelin = fread($fnotelin,filesize($lnotelin));
fclose($fnotelin);

// note log :
$fnotelog = fopen($lnotelog, "r");
$notelog = fread($fnotelog,filesize($lnotelog));
fclose($fnotelog);

// note inv :
$fnoteinv = fopen($lnoteinv, "r");
$noteinv = fread($fnoteinv,filesize($lnoteinv));
fclose($fnoteinv);

// note car :
$fnotecar = fopen($lnotecar, "r");
$notecar = fread($fnotecar,filesize($lnotecar));
fclose($fnotecar);

$fmod = fopen($lmod, "r");
$mod = fread($fmod,filesize($lmod));
fclose($fmod);


switch ($mod) {
    case "lin":
        $note = $notelin;
        break;
    case "log":
        $note = $notelog;
        break;
    case "inv":
        $note = $noteinv;
        break;
    case "car":
        $note = $notecar;
        break;
}



$fnom = fopen($lnom, "r");
$nom = fread($fnom,filesize($lnom));
fclose($fnom);
?>





    <head>
		<link rel="shortcut icon" type="image/png" href="img/logo.png"/>
		<link rel="stylesheet" type="text/css" href="style.css">
		<meta http-equiv= "content-type" content= "text/html; charset=UTF-8" >
        <title> Institut Villebon Charpak </title>
        <script src="index.js"></script>
    </head>

    <body onresize="changeHeight()" onload="changeHeight()" onscroll="hidemain()">
        <div class="main" id="main">
            <img class="bg" src="img/bg.jpg" alt="Institut Villebon Charpak">
                <div class="title">
                    <h1>
                        Institut Villebon Charpak
                    </h1>
                    <h2>
                        Notations
                    </h2>
                </div>
        </div>

        <h1>
            <center>
                Bonjour <?php echo $nom; ?>
            </center>
        </h1>
        <div class="content" id="content">

            <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
            <br><br>
            <p>
                <?php
                echo $note;
                ?>
            </p>
            <br><br>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
        </div>

    </body>
</html>
