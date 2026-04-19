# ⚠️ AVISO LEGAL Y LIMITACIÓN DE RESPONSABILIDAD

OmniGroup es un holding empresarial ficticio CHILENO, creado exclusivamente con fines académicos y de laboratorio profesional. El contenido, las estructuras corporativas, los datasets y las situaciones de riesgo presentadas en este repositorio son simulaciones diseñadas para la demostración práctica de modelos de cumplimiento (Compliance) y protección de datos.

Este entorno funciona como un "Sandbox de Cumplimiento" para la implementación de las Leyes 21.719 y 21.663 en Chile, y no guarda relación alguna con empresas, personas naturales o datos reales existentes.
# 🛡️ OmniGroup Compliance Lab: Gestión de Crisis y Riesgo Normativo

Este repositorio documenta la intervención integral de **Compliance y Protección de Datos** realizada sobre el Holding **OmniGroup**, ante el riesgo inminente de multas gravísimas bajo la **Ley 21.719** y la **Ley 21.663** en Chile.

## 🏢 Estructura del Holding

El ecosistema de OmniGroup está compuesto por cuatro unidades de negocio con flujos de datos interconectados:

1. **OmniSalud (Clínica):** Gestión de datos sensibles, fichas clínicas y telemedicina.
2. **OmniBank (Banca Digital):** Activos financieros críticos y ciberseguridad transaccional.
3. **OmniRobotics (IA):** Desarrollo de asistentes robóticos con recolección masiva de audio/video.
4. **OmniRetail & Seguros:** Fidelización de clientes y perfilamiento de consumo.

## 🌋 El Escenario de Crisis (Diagnóstico)

Tras una auditoría inicial, se han detectado fallas críticas que exponen al Directorio a multas de hasta **20.000 UTM** por cada entidad:

- **Contaminación Cruzada:** El Retail está utilizando datos de salud y bancarios para perfilar seguros de vida sin consentimiento expreso.
- **Vulnerabilidad en IA:** Robots de asistencia sin Evaluación de Impacto (DPIA) ni gestión de sesgos algorítmicos.
- **Brecha de Seguridad:** Ausencia de protocolos de reporte ante la nueva Agencia Nacional de Ciberseguridad.

## ⚖️ Objetivo del Proyecto

Implementar un modelo de **Privacidad desde el Diseño (PbD)**, realizar los DPIA correspondientes y establecer los controles de ciberseguridad necesarios para blindar legal y reputacionalmente al Holding.
# Inventario y Caracterización de Activos de Datos - Proyecto OmniGroup

Este documento detalla la estructura y naturaleza de los datasets utilizados en el entorno de simulación del Holding OmniGroup. Estos activos constituyen la base empírica para la auditoría de cumplimiento bajo la Ley 21.719 de Protección de Datos Personales y la Ley 21.663, Ley Marco de Ciberseguridad en Chile.

## 1. OmniSalud: Gestión de Datos Sensibles

Este dataset simula el repositorio de una entidad prestadora de servicios de salud. Es el activo con mayor nivel de protección debido a la naturaleza de su contenido.

* **Identificador de Archivo:** `omnisalud_clientes.csv`
* **Categoría de Datos:** Datos sensibles (Art. 2, letra g, Ley 21.719).
* **Campos Críticos:**
    * `ID_Interno`: Identificador único persistente del titular.
    * `Nombre_Paciente`: Datos identificativos del usuario.
    * `Patologia_Cronica`: Diagnósticos médicos y antecedentes de salud.
* **Propósito de Cumplimiento:** Evaluar el respeto al principio de finalidad y las medidas de seguridad para datos cuya filtración supone un riesgo alto para los derechos y libertades.

## 2. OmniBank: Activos Financieros y Riesgo

Dataset representativo de la unidad de banca digital del holding, enfocado en la solvencia y seguridad transaccional.

* **Identificador de Archivo:** `omnibank_clientes.csv`
* **Categoría de Datos:** Datos personales de carácter financiero y económico.
* **Campos Críticos:**
    * `ID_Interno`: Clave primaria vinculada al holding.
    * `Saldo_Promedio`: Información de activos financieros.
    * `Score_DICOM`: Calificación de riesgo crediticio.
    * `Estado_Ciberseguridad`: Indicador de protocolos de acceso del usuario.
* **Propósito de Cumplimiento:** Analizar la integridad de los datos financieros y el cumplimiento del secreto bancario frente a la interconexión de filiales.

## 3. OmniRobotics: Inteligencia Artificial y Biometría

Dataset técnico orientado al desarrollo de asistentes domésticos mediante IA, captación de datos biométricos y telemetría.

* **Identificador de Archivo:** `omnirobotics_activos.csv`
* **Categoría de Datos:** Datos biométricos e información de infraestructura crítica.
* **Campos Críticos:**
    * `ID_Dispositivo`: Identificación de hardware IoT.
    * `Recoleccion_Biometrica`: Indicador de captación de rostro y voz (ISO 42001).
    * `Cifrado_Punto_a_Punto`: Estado de la seguridad en la transmisión (Ley 21.663).
* **Propósito de Cumplimiento:** Implementar controles de "Privacy by Design" y evaluar riesgos de acceso no autorizado a la intimidad del hogar.

## 4. OmniRetail & Seguros: Perfilamiento y Consumo

Dataset de ejecución comercial donde convergen los flujos de datos del holding para la toma de decisiones automatizadas.

* **Identificador de Archivo:** `omniretail_clientes.csv`
* **Categoría de Datos:** Datos de comportamiento de consumo y perfiles actuariales.
* **Campos Críticos:**
    * `Gasto_Mensual`: Patrones de consumo del cliente.
    * `Seguro_Vida_Estado`: Decisión de adjudicación (Aprobado/Rechazado).
    * `Motivo_Decision`: Justificación técnica de la evaluación de riesgo.
* **Propósito de Cumplimiento:** Detectar la "contaminación cruzada" de datos. Es el punto crítico para el análisis de discriminación algorítmica y la transparencia en decisiones automatizadas.

---

## Metodología de Auditoría

La interconexión de estos datasets mediante el campo `ID_Interno` permite realizar un peritaje forense de datos para cuantificar el impacto de la vulneración de la privacidad. Este inventario es el insumo principal para la elaboración del DPIA según los estándares de la AEPD. En vinculación directa con Chile y APDP, Ley 21.719