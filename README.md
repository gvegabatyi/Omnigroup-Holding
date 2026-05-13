$content = @"
# OmniGroup Holding: Compliance & GRC Lab

Este repositorio documenta la intervención integral de auditoría y cumplimiento normativo realizada sobre el Holding ficticio **OmniGroup**, bajo el marco legal chileno (**Ley 21.719** y **Ley 21.663**).

## Marco Normativo y Estándares Aplicados
* **Ley 21.719:** Nueva Ley de Protección de Datos Personales en Chile.
* **Ley 21.663:** Ley Marco de Ciberseguridad e Infraestructura Crítica.
* **ISO 27001 / 27701:** Gestión de Seguridad y Privacidad de la Información.
* **ISO 42001:** Gestión de Inteligencia Artificial.

## Entregable Oficial
El dictamen consolidado con los hallazgos, matrices de riesgo y el roadmap de cumplimiento se encuentra disponible en el siguiente enlace:

* [**Descargar Reporte Ejecutivo OmniGroup (PDF)**](./Holding_Omigroup.pdf)

---
**Consultor:** Gonzalo Vega Batyi | Abogado experto en GRC, Protección de Datos y Ciberseguridad.
"@

Set-Content -Path README.md -Value $content -Encoding utf8
