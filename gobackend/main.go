package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// Simple root API
	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "✅ Go backend is running",
		})
	})

	r.Run(":8080") // localhost:8080
}
   