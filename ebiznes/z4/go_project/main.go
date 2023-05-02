package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}

func main() {
	db, err := gorm.Open(sqlite.Open("products.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	db.AutoMigrate(&Product{})

	e := echo.New()

	e.POST("/products", func(c echo.Context) error {
		p := new(Product)
		if err := c.Bind(p); err != nil {
			return err
		}

		db.Create(&p)

		return c.JSON(http.StatusCreated, p)
	})

	e.GET("/products/:id", func(c echo.Context) error {
		id := c.Param("id")

		var p Product
		if err := db.First(&p, id).Error; err != nil {
			return err
		}

		return c.JSON(http.StatusOK, p)
	})

	e.PUT("/products/:id", func(c echo.Context) error {
		id := c.Param("id")

		var p Product
		if err := db.First(&p, id).Error; err != nil {
			return err
		}

		if err := c.Bind(&p); err != nil {
			return err
		}

		db.Save(&p)

		return c.JSON(http.StatusOK, p)
	})

	e.DELETE("/products/:id", func(c echo.Context) error {
		id := c.Param("id")

		var p Product
		if err := db.First(&p, id).Error; err != nil {
			return err
		}

		db.Delete(&p)

		return c.NoContent(http.StatusNoContent)
	})

	e.GET("/products", func(c echo.Context) error {
		var products []Product
		if err := db.Find(&products).Error; err != nil {
			return err
		}

		return c.JSON(http.StatusOK, products)
	})

	e.Logger.Fatal(e.Start(":8080"))
}
