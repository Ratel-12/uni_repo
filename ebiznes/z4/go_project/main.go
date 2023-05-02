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
	// Connect to the database
	db, err := gorm.Open(sqlite.Open("products.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	// Migrate the schema
	db.AutoMigrate(&Product{})

	// Create a new Echo instance
	e := echo.New()

	// Create a new product
	e.POST("/products", func(c echo.Context) error {
		// Parse the request body
		p := new(Product)
		if err := c.Bind(p); err != nil {
			return err
		}

		// Save the product to the database
		db.Create(&p)

		return c.JSON(http.StatusCreated, p)
	})

	// Retrieve a product
	e.GET("/products/:id", func(c echo.Context) error {
		// Get the product ID from the URL params
		id := c.Param("id")

		// Find the product in the database
		var p Product
		if err := db.First(&p, id).Error; err != nil {
			return err
		}

		return c.JSON(http.StatusOK, p)
	})

	// Update a product
	e.PUT("/products/:id", func(c echo.Context) error {
		// Get the product ID from the URL params
		id := c.Param("id")

		// Find the product in the database
		var p Product
		if err := db.First(&p, id).Error; err != nil {
			return err
		}

		// Parse the request body
		if err := c.Bind(&p); err != nil {
			return err
		}

		// Update the product in the database
		db.Save(&p)

		return c.JSON(http.StatusOK, p)
	})

	// Delete a product
	e.DELETE("/products/:id", func(c echo.Context) error {
		// Get the product ID from the URL params
		id := c.Param("id")

		// Find the product in the database
		var p Product
		if err := db.First(&p, id).Error; err != nil {
			return err
		}

		// Delete the product from the database
		db.Delete(&p)

		return c.NoContent(http.StatusNoContent)
	})

	// List all products
	e.GET("/products", func(c echo.Context) error {
		// Find all products in the database
		var products []Product
		if err := db.Find(&products).Error; err != nil {
			return err
		}

		return c.JSON(http.StatusOK, products)
	})

	// Start the server
	e.Logger.Fatal(e.Start(":8080"))
}
