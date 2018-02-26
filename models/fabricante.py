from odoo import models, fields

class fabricante(models.Model):
    _name = 'ordenadores.fabricante'
    codigo = fields.Integer('Codigo de fabricante', required=True)
    nombre = fields.Char('Nombre del fabricante', required=True)
    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

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