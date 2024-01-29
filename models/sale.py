from odoo import models, fields, api
from odoo.exceptions import ValidationError



class new_one(models.Model):
    _inherit="sale.order.line"


    new_on=fields.Char("newaddes",compute="_compute_new")
    internal = fields.Char("Internal Refrence")


    def _compute_new(self):
        for rec in self:
            rec.new_on=rec.product_template_id.name


    @api.onchange('product_template_id')
    def _onchange_internal(self):
        self.internal = self.product_template_id.categ_id.name
        # self.product_template_id.barcode = "juke ga nay sala"

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    var = fields.Char("Order")

 
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res["var"]="hello"
        print("res:::::::::::::::::",res)
        return res

# class PurchaseOrderLine(models.Model):
#     _inherit = 'purchase.order.line'

#     def write(self,vals):
#         if "price_unit" in vals:
#             record=self.order_id
#             record.message_post(body=f"sir ji {vals['price_unit']}")
#         res = super().write(vals)
#         return res


# class ProductTemplate(models.Model):
#     _inherit = 'product.template'

#     @api.model
#     def _name_search(self, name="", args=None, operator='ilike', limit=100, name_get_uid=None):
#         print("----------------------------------_>",name)
#         args = args or []
#         domain = []
#         domain = [('categ_id', operator, "Office Furniture")]
#         return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    show = fields.Boolean("Show")
    month = fields.Float("Month")
    date = fields.Date("Date")
    amount = fields.Float("Amount")

    def action_confirm(self):
        res=super(SaleOrder,self).action_confirm()
        if self.show == True:
            self.picking_ids.is_show=True
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if self.show == False:
            self.picking_ids.is_show = False
        return res

    def action_emi_system(self):
        print("::::::::::::::::::::::::::::::")

class StockPicking(models.Model):
    _inherit = "stock.picking"

    is_show = fields.Boolean("Is pending",readonly=1)

    def button_validate(self):
        if self.is_show == True:
            raise ValidationError(f"This {self.origin} not switch to done state!")
        res = super().button_validate()
        return res 