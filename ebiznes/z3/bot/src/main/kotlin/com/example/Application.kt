package com.example

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import com.example.plugins.*
import dev.kord.core.Kord
import dev.kord.core.on
import dev.kord.core.event.message.MessageCreateEvent
import dev.kord.gateway.Intent
import dev.kord.gateway.PrivilegedIntent

data class Category(val id: Int, var name: String, val items: List<String>)

suspend fun main() {
    val kord = Kord("TOKEN_HERE")
    val categoriesList = listOf<Category>(
        Category(1, "fruits", listOf("apple", "orange", "banana")),
        Category(2, "fish", listOf("cod", "tuna", "salmon")),
        Category(3, "sodas", listOf("mountain dew", "coca cola", "sprite"))
    )

    kord.on<MessageCreateEvent> {
        if (message.author?.isBot != false) return@on
        if (message.content.startsWith("!category")) {
            val regex = Regex("!category (.+)")
            val result = regex.find(message.content)

            if (result != null) {
                val query = result.groupValues[1]
                var category = categoriesList.find { it.name == query }
                var printString = "Displaying items in category \"$query\":\n"
                category?.items?.forEach {
                    item -> printString += "    ${item}\n"
                }
                message.channel.createMessage(printString)
            }
            else message.channel.createMessage("No such category.\n")
        }
        if (message.content == "!categories") {
            var printString = "Categories:\n"
            categoriesList.forEach {
                category -> printString += "    ${category.id}: ${category.name}\n"
            }
            message.channel.createMessage(printString)
        }
        if (message.content == "!commands") {
            var messageText = "commands:\n"
            messageText += "    !commands -> You are reading the result. You know what it does.\n"
            messageText += "    !categories -> Displays all viable categories.\n"
            messageText += "    !category <NAME_OF_THE_CATEGORY> -> Displays all items from a given category.\n"
            message.channel.createMessage(messageText)
        }
    }

    kord.login {
        @OptIn(PrivilegedIntent::class)
        intents += Intent.MessageContent
    }
}

fun Application.module() {
    configureRouting()
}
