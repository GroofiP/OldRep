<?php
    $name = $_POST["username"];
    $email = $_POST["email"];
    $pass = $_POST["password"];
    $message = $_POST["message"];

    if (trim($name) == "")
        echo "Вы не ввели имя пользователя";
    else if (strlen(trim($name)) <= 2)
        echo "Такое имя не существует";
    else if (!trim($email) || !trim($pass) || !trim($message))
        echo "Введите все данные";
    else
        header("Location: about.php");
        exit;