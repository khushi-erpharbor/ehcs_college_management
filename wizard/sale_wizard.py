from odoo import fields, models


class Sale(models.TransientModel):
    _name = "sale.sale"
    _description = "sale"

    product_template_id = fields.Many2one("product.template",string="Product")

    def action_submit_stud(self):
        model=self.env.context.get('active_model')
        ids=self.env.context.get('active_id')
        record=self.env[model].browse(ids)
        print(record,"                     ------               ")
        record={"product_template_id":self.product_template_id.id}
        print("\n\n\n\n\n\n\n\nreorcs::::::::::::::::::::::::::::",record)
        result = record.update({
            'order_line': [(fields.Command.create({"product_template_id":self.product_template_id.id }))]
        })
        print(result)
        # print("\n\n\n\n\n\n\n\nresult::::::::::::::::::::::::::::",result)


        # ctx = self.env.context
        # print("CTX::::::::::::::::::::::::::::",ctx)
        # if ctx.get('active_model') == 'sale.order' and ctx.get('active_id'):
        #     result_dict = {'product_template_id': ctx.get('active_id'), 'product_template_id': self.product_template_id.id}
        #     print('\n\n result_dict',result_dict)
        #     result = self.env['sale.order.line'].create(result_dict)
        #     print('\n\n result', result)
                                                           
