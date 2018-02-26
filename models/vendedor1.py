from odoo import models, fields

class vendedor1(models.Model):
    _name = 'ordenadores.vendedor1'
    vendedor = fields.Char('Vendedor', required=True)
    fabricante = fields.Many2one('ordenadores.fabricante', 'Fabricante')

    def name_get(self):
        res=[]
        for record in self:
            name = record.vendedor
            res.append((record.id, name))
        return res