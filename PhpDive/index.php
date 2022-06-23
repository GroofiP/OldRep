<?php
$title = "Главная";
include_once "includes/header.php";
?>

    <h1>Главная</h1>
    <form method="get" action="check_get.php">
        <input name="text" type="text">
        <input type="submit" value="Найти">
    </form>

<?php
include_once "includes/footer.php";
?>