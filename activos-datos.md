# Expediente de Cumplimiento: OmniSalud 🏥

Este documento presenta el análisis técnico-jurídico del tratamiento de datos sensibles en la filial de salud del holding.

---

## 🔍 1. Auditoría de Cumplimiento (Compliance)
Se auditó el flujo de datos de telemedicina bajo el estándar de la **Ley 21.719**.
* **Hallazgo:** Uso de plataformas de videollamada de terceros sin contratos de encargado de tratamiento (Art. 25).
* **Base Legal:** El tratamiento actual carece de una política de "Privacidad desde el Diseño" (Privacy by Design), exponiendo datos de fichas clínicas en servidores fuera del territorio nacional sin las debidas salvaguardas.

## ⚠️ 2. Matriz de Riesgos (Risk Management)
Basado en un enfoque de gestión de riesgos para el Directorio:
* **Riesgo Legal:** Infracción gravísima por tratamiento de datos sensibles (salud) sin medidas de seguridad proporcionales (Multas hasta 20.000 UTM).
* **Riesgo Operativo:** Falta de protocolos de notificación de brechas de seguridad ante la futura Agencia (APDP), lo que aumenta la exposición a sanciones acumulativas.
* **Impacto:** Crítico para la continuidad del negocio en caso de Ransomware.

## ⚙️ 3. Protocolos de Tratamiento
Se proponen los siguientes mecanismos de control:
* **Seudonimización:** Disociación de datos identificatorios (RUT, Nombres) de los datos diagnósticos para análisis estadísticos del holding.
* **Gobernanza de Acceso:** Implementación de protocolos de autenticación multifactor (MFA) para el acceso a la base de datos de pacientes.
* **Minimización:** Eliminación de campos innecesarios en los formularios de registro inicial.

## 📌 4. Conclusiones y Recomendaciones
1. **Nombramiento de DPO:** Es mandatorio un Oficial de Protección de Datos que supervise la segregación de bases de datos entre OmniSalud y OmniRetail.
2. **Evaluación de Impacto (DPIA):** Realizar un DPIA semestral sobre los nuevos sistemas de diagnóstico asistido por IA.
3. **Accountability:** Formalizar el Registro de Actividades de Tratamiento (RAT) para acreditar cumplimiento ante fiscalizaciones externas.

---
[⬅️ Volver al Inventario Principal](./activos-datos.md)