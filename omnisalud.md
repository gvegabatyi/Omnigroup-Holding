# Informe de Cumplimiento: OmniSalud 🏥

[Auditoría](#auditoria) | [Riesgos](#riesgos) | [Tratamiento](#tratamiento) | [Conclusiones](#conclusiones)

---

<a name="auditoria"></a>
## 🔍 1. Auditoría de Cumplimiento
Se realizó una revisión de los procesos de captura de datos en la plataforma de telemedicina. 
* **Hallazgo:** Los formularios no diferencian claramente entre datos administrativos y datos de salud sensibles.
* **Estándar:** Incumplimiento del Art. 9 de la Ley 21.719.

<a name="riesgos"></a>
## ⚠️ 2. Matriz de Riesgos
* **Riesgo Operativo:** Fuga de fichas clínicas por falta de cifrado en tránsito.
* **Riesgo Legal:** Multas de hasta 20.000 UTM por tratamiento de datos sensibles sin base de licitud clara.
* **Probabilidad:** Alta.

<a name="tratamiento"></a>
## ⚙️ 3. Protocolos de Tratamiento
Se propone la **Seudonimización** inmediata de la base de datos de pacientes antes de ser compartida con el motor de analítica del holding. El tratamiento debe basarse estrictamente en la "Ejecución del contrato de salud".

<a name="conclusiones"></a>
## 📌 4. Conclusiones y Recomendaciones
Es imperativo nombrar un Delegado de Protección de Datos (DPO) exclusivo para el área de salud y actualizar los avisos de privacidad para cumplir con el estándar de transparencia de la nueva Agencia (APDP).

---
[⬅️ Volver al Inventario Principal](./activos-datos.md)