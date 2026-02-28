package com.automation;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class firstauto {

    public static void main(String[] args) {

        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

        driver.get("https://www.damsdelhi.com/");

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));

        // =========================
        // Fill Name
        // =========================
        WebElement name = wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.name("name")));
        name.sendKeys("Brijesh Singh");

        // =========================
        // Fill Email
        // =========================
        driver.findElement(By.name("email"))
                .sendKeys("brijesh@gmail.com");

        // =========================
        // Fill Mobile Number
        // =========================
        wait.until(ExpectedConditions.visibilityOfElementLocated(
        By.xpath("//input[@placeholder='Mobile Number']")))
    .sendKeys("9876543210");

        // =========================
        // Select NEET PG/NEXT (if dropdown)
        // =========================
        wait.until(ExpectedConditions.visibilityOfElementLocated(
        By.xpath("//*[contains(text(),'NEET')]")))
    .click();


        // =========================
        // Enter Query
        // =========================
        driver.findElement(By.xpath("//textarea[contains(@placeholder,'Type your query')]"))
                .sendKeys("I want more details about the course.");

        // ================

    }

}