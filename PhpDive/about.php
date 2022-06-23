<?php
$title = "О нас";
include_once "includes/header.php";
?>

<div class="container mt-2 mb-2">
<h1>О нас</h1>
    <form action="check_post.php" method="post">
        <input name="username" type="text" placeholder="Введите имя" class="form-control">
        <input name="email" type="email" placeholder="Введите email" class="form-control">
        <input name="password" type="password" placeholder="Введите пароль" class="form-control">
        <textarea name="message" placeholder="Введите сообщение" class="form-control"></textarea>
        <input value="Отправить" type="submit" class="btn btn-success">
    </form>
</div>
<?php
include_once "includes/footer.php";
?>