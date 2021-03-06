from odoo import models, fields, api

class placasbase(models.Model):
    _name = 'ordenadores.placasbase'
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
    especificaciones = fields.Char('Especificaciones', required=True)
    precio = fields.Char('Precio', required=True)
    fabricante = fields.Many2one('ordenadores.fabricante', 'Fabricante')
    vendedor = fields.Many2one('ordenadores.vendedor1', 'Vendedor')

    @api.one
    def limpiar(self):
        self.marca = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('marca', '=', 'asus')])
        done_recs.write({'marca': 'Asus'})
        return True