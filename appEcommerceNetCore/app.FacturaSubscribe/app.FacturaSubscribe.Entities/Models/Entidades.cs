using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace app.FacturaSubscribe.Entities.Models
{
    public class Categoria
    {
        public int Id { get; set; }
        public string? Nombre { get; set; }
        public string? Descripcion { get; set; }
        public bool Estado { get; set; }
        public DateTime Fecha { get; set; }
    }

    public class Factura
    {
        public int Id { get; set; }
        public string? Cliente { get; set; }
        public string? Producto { get; set; }
        public int Cantidad { get; set; }
        public string? Categoria { get; set; }
        public decimal Valor { get; set; }
        public decimal Total { get; set; }
    }

}
