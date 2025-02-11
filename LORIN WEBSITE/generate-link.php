<?php
$token = "CorsicaFerries911"; // Dein fester Token

// Falls kein Token in der URL ist, leite um
if (!isset($_GET['token']) || $_GET['token'] !== $token) {
    header("Location: index.html?token=$token");
    exit();
}
?>

