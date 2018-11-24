<!DOCTYPE html>
<html>
<?php
session_start();


if(isset($_SESSION["eleve"]))
{
    $n = $_SESSION["eleve"];
}
else
{
    header("Location: index.php");
    die();
}
$l = "Data/" . $n;
$s = "Data/Settings/";
$lmod = $s . "modele.txt";
$lnbrcontroles = $s . "nbrcontroles.txt";


$lnom   = $l . "/prenom.txt";
$lcitationperso = $l . "/citation.txt";



$lxp   = $l . "/xp";
$lxp1 = $lxp . "1.txt";
$lxp2 = $lxp . "2.txt";
$lxp3 = $lxp . "3.txt";
$lxp4 = $lxp . "4.txt";


$lnotelin = $l . "/note.txt";
$lnotelog = $l . "/notel.txt";
$lnoteinv = $l . "/notei.txt";
$lnotecar = $l . "/notec.txt";

// XP

$fxp1 = fopen($lxp1, "r");
$xp1 = fread($fxp1,filesize($lxp1));
fclose($fxp1);

$fxp2 = fopen($lxp2, "r");
$xp2 = fread($fxp2,filesize($lxp2));
fclose($fxp2);

$fxp3 = fopen($lxp3, "r");
$xp3 = fread($fxp3,filesize($lxp3));
fclose($fxp3);

$fxp4 = fopen($lxp4, "r");
$xp4 = fread($fxp4,filesize($lxp4));
fclose($fxp4);





$fcitationperso = fopen($lcitationperso, "r");
$citationperso = utf8_encode(fread($fcitationperso,filesize($lcitationperso)));
fclose($fcitationperso);





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




$fnbrcontroles = fopen($lnbrcontroles, "r");
$nbrcontroles = fread($fnbrcontroles,filesize($lnbrcontroles));
fclose($fnbrcontroles);


if((float)$note<10)
{
    $fond = "\"img/fond_moins_10.jpg\"";
    $lcitationsnote = "citations_moins_10.txt";
}
elseif((float)$note<13)
{
    $fond = "\"img/fond_10-13.jpg\"";
    $lcitationsnote = "citations_10-13.txt";
}
elseif((float)$note<16)
{
    $fond = "\"img/fond_13-16.jpg\"";
    $lcitationsnote = "citations_13-16.txt";
}
else
{
    $fond = "\"img/fond_plus_16.jpg\"";
    $lcitationsnote = "citations_plus_16.txt";
}

$fcitationsnote = fopen($lcitationsnote, "r");
$citationsnote = utf8_encode(fread($fcitationsnote,filesize($lcitationsnote)));
fclose($fcitationsnote);


$citationsnote = explode("\n",$citationsnote);

$r = random_int(0,5);


$citationnote = $citationsnote[3*$r]."<br>".$citationsnote[3*$r+1];





?>





    <head>
		<link rel="shortcut icon" type="image/png" href="img/logo.png"/>
		<link rel="stylesheet" type="text/css" href="notes.css">
		<meta http-equiv= "content-type" content= "text/html; charset=utf-8" >
        <title> Institut Villebon Charpak </title>
        <script src="notes.js"></script>
        <style media="screen">
            .content{background-image: url(<?php echo $fond ?>);}
        </style>
    </head>

    <body onresize="changeHeight()" onload="changeHeight()" onscroll="hidemain()">


        <div class="content" id="content">
            <h1 class="titre">
                <center>
                    Bonjour <?php echo $nom; ?>
                </center>
            </h1>
            <div class="blockgauche">
                <br>
                <div class="noteglobale">
                    <p>
                        Votre note est pour l'instant de : <?php echo $note; ?> /20. <br>
                        Il reste normalement encore <?php echo $nbrcontroles; ?> contrôles pour augmenter votre note. <br>
                    </p>
                </div>
                <br><br>
                <div class="rankxp">
                    <p>
                        Voici vos XPs : <br>
                        Theme 1 : <?php echo $xp1; ?> <br>
                        Theme 2 : <?php echo $xp2; ?> <br>
                        Theme 3 : <?php echo $xp3; ?> <br>
                        Theme 4 : <?php echo $xp4; ?> <br>
                    </p>
                </div>
                <br><br>
                <div class="citationPerso">
                    <?php echo $citationperso ?>
                </div>
                <br>
            </div>
            <div class="graphs">

            </div>
            <br>
            <div class="citationNote">
                <?php echo $citationnote ?>
            </div>
        </div>
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
                <br>
    </body>
</html>
