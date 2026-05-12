# Informe de Verificación de Infraestructura y Trazabilidad de Datos

**Fecha:** 12 de mayo de 2026  
**Auditor:** Gonzalo Vega Batyi  
**Cargo:** Abogado Experto en GRC & Protección de Datos (Hybrid Lawyer)  
**Proyecto:** Omnigroup Holding - Auditoría de cumplimiento técnico-legal  

---

## 1. Resumen Ejecutivo
El presente informe documenta el ejercicio de verificación perimetral y trazabilidad de rutas sobre el activo de red **1.1.1.1** (Cloudflare/APNIC). El objetivo es validar la visibilidad pública de un servicio de infraestructura crítica y analizar las implicancias jurídicas de su configuración bajo el marco de la **Ley 21.663** (Ley Marco de Ciberseguridad) y la **Ley 21.719** (Protección de Datos Personales).

## 2. Metodología de Auditoría (Ética y No Intrusiva)
Se aplicó un enfoque de **"Caja Negra"** limitado a la obtención de información pública y diagnóstico de red, respetando el principio de legalidad y evitando cualquier acción que pudiera comprometer la disponibilidad del servicio.

### Herramientas utilizadas:
* **WHOIS:** Identificación de titularidad y jurisdicción.
* **NMAP:** Mapeo de puertos para análisis de superficie de ataque.
* **TRACEROUTE:** Análisis de saltos para verificar transferencia internacional de datos.

---

## 3. Resultados del Peritaje

### A. Identificación de Jurisdicción (WHOIS)
* **Hallazgo:** El activo está registrado bajo el RIR **APNIC** (Australia).
* **Implicancia Legal:** Existe una triangulación de gobernanza de datos que involucra a Australia y EE.UU. como responsables técnicos. Para el cumplimiento de la **Ley 21.719**, esto exige verificar la existencia de cláusulas contractuales adecuadas para el tratamiento transfronterizo.

### B. Análisis de Superficie de Ataque (NMAP)
* **Resultado:** 995 puertos filtrados (no-response).
* **Puertos Abiertos:** 53 (DNS), 80/443 (HTTP/S), 8080/8443 (Proxy/Alt).
* **Dictamen Técnico:** Se observa cumplimiento del **Principio de Exposición Mínima**. El filtrado masivo indica una defensa perimetral activa (Firewall) que mitiga riesgos de reconocimiento ilícito.

### C. Mapeo de Ruta y Latencia (TRACEROUTE)
* **Resultado:** 7 saltos desde el nodo de origen. Latencia promedio de **10.9 ms**.
* **Dictamen de Cumplimiento:** La baja latencia confirma que el flujo de datos se mantiene dentro de la región geográfica local (Peering directo), minimizando la exposición de los datos en nodos intermedios de terceros países de bajo nivel de protección.

---

## 4. Conclusiones de Compliance
Desde la perspectiva de un **Data Protection Officer (DPO)**, la infraestructura auditada presenta un nivel de seguridad conforme al "estado del arte". La transparencia en la identificación de contactos de abuso y la restricción de puertos visibles son evidencias de **Privacidad desde el Diseño (Privacy by Design)**.

---

## 5. Declaración de Integridad
Este ejercicio ha sido realizado con fines estrictamente académicos y de perfeccionamiento profesional. No se han vulnerado medidas de seguridad ni se ha accedido a sistemas de información de manera indebida (Art. 1, Ley 21.459).