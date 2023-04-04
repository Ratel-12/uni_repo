package controllers

import javax.inject._
import play.api._
import play.api.mvc._
import play.api.libs.json._
import scala.collection.mutable
import internals.ProductClass

@Singleton
class ProductsController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
  implicit var products = new mutable.ListBuffer[ProductClass]()
  products += ProductClass(0, "something0", 21.37, "something of variety 0")
  products += ProductClass(1, "something1", 21.37, "something of variety 1")
  products += ProductClass(2, "something2", 21.37, "something of variety 2")
  implicit var productJson: OFormat[ProductClass] = Json.format[ProductClass]

  def getAll(): Action[AnyContent] = Action {
    if (products.isEmpty) {
      NoContent
    } else {
      Ok(Json.toJson(products))
    }
  }
}
