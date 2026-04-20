# ⚠️ AVISO LEGAL Y LIMITACIÓN DE RESPONSABILIDAD

OmniGroup es un holding empresarial ficticio CHILENO, creado exclusivamente con fines académicos y de laboratorio profesional. El contenido, las estructuras corporativas, los datasets y las situaciones de riesgo presentadas en este repositorio son simulaciones diseñadas para la demostración práctica de modelos de cumplimiento (Compliance) y protección de datos.
Este laboratorio busca ilustar situaciones complejas que son necesarias de abordar, por cierto, de forma colectiva en una organización con equipos multidiciplinarios con visión de mejora continua.

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

La interconexión de estos datasets mediante el campo `ID_Interno` permite realizar un **peritaje forense de datos** para cuantificar el impacto de la vulneración de la privacidad. Este inventario es el insumo principal para la elaboración del **DPIA** según los estándares de la **AEPD**. En vinculación directa con Chile y APDP, *Ley 21.719*

## 📋 Plan de Auditoría de Gobernanza y Gestión de Riesgos: Holding OmniGroup

**Responsable:** Gonzalo Vega Batyi, Abogado / DPO

**Referencia Metodológica:** ISO 31000 (Riesgo), ISO 27001 (SGSI), ISO 27701 (SGPI)

**Normativa Primaria:** Ley 21.719 (Protección de Datos) y Ley 21.663 (Ciberseguridad)

**Modelos de Referencia:** AEPD (Sector Privado) / EDPB Template 2026

### 1. Diagnóstico de Situación: El Vacío Normativo

Tras el análisis forense de los datasets, se identifica que el Holding OmniGroup carece de una infraestructura de cumplimiento documental y operativa. No existe una cultura de **Responsabilidad Proactiva (Accountability)**, lo que genera una exposición crítica ante la autoridad de control.

#### 1.1 Ausencia de Controles Organizativos

Se ha verificado la inexistencia de:

- **Manual de Políticas de Privacidad:** No hay directrices que regulen el ciclo de vida del dato.
- **Protocolos de Gestión de Datos Sensibles:** La información de OmniSalud fluye sin restricciones hacia áreas comerciales.
- **Directrices de Seguridad (SGSI):** Ausencia de estándares de cifrado y control de accesos en activos críticos.
- **Manuales de Procedimiento para IA:** El desarrollo de OmniRobotics no contempla gestión de sesgos ni transparencia algorítmica.

### 2. Alcance de la Auditoría (Scope)

El alcance se define por la interconectividad detectada en el **Reporte Maestro** (404 ciudadanos vulnerados). La auditoría se centrará en los siguientes puntos críticos por empresa:

#### A. OmniSalud (Privacidad y Ética Clínica)
- Evaluación de la base legal para la transferencia de datos sensibles.
- Auditoría del principio de limitación de la finalidad (*Art. 9, Ley 21.719*).

#### B. OmniBank (Integridad y Secreto Bancario)
- Verificación de medidas de seguridad en la transmisión de datos financieros.
- Control de segregación de bases de datos para evitar fugas hacia Retail.

#### C. OmniRobotics (IA y Seguridad Técnica)
- Análisis de los protocolos de cifrado en telemetría (*Ley 21.663*).
- Evaluación de impacto ético y biométrico basado en las guías de auditoría IA de la AEPD.

#### D. OmniRetail & Seguros (Transparencia y No Discriminación)
- Auditoría de decisiones automatizadas y perfiles de riesgo.
- Detección de contaminación cruzada de datos para fines actuariales.

### 3. Metodología de Trabajo (Skeleton ISO)

Para remediar el escenario de crisis, el orden de trabajo se ajustará a la siguiente jerarquía normativa:

#### Fase I: Identificación (ISO 31000)
Uso del modelo de gestión de riesgos para identificar eventos que afecten los derechos y libertades de los interesados. Evaluación de la probabilidad e impacto de las multas de *20.000 UTM*.

#### Fase II: Seguridad de la Información (ISO 27001 - SGSI)
Establecimiento de controles de seguridad (**Confidencialidad, Integridad y Disponibilidad**) sobre los activos de información del holding, con especial énfasis en el cifrado y la autenticación.

#### Fase III: Gestión de la Privacidad (ISO 27701 - SGPI)
Implementación de los controles específicos del Responsable del Tratamiento para asegurar el cumplimiento de la *Ley 21.719* y la adecuada respuesta al ejercicio de derechos por parte de los titulares.

### 4. Objetivos Estratégicos del Proyecto

- **Saneamiento de Base de Datos:** Eliminar la persistencia del identificador único y establecer seudonimización.
- **Generación de DPIA:** Elaborar las evaluaciones de impacto definitivas.
- **Blindaje Jurídico:** Crear los manuales y directrices que acrediten que el Directorio ha tomado medidas razonables de control para mitigar la responsabilidad penal y administrativa.
# Estructura Organizativa y Modelo de Gobernanza - OmniGroup

Para garantizar la **Responsabilidad Proactiva (Accountability)** y la segregación de funciones exigida por las normas **ISO 27001** (SGSI) e **ISO 27701** (SGPI), el Holding OmniGroup opera bajo una estructura jerárquica simétrica. Este diseño asegura que cada unidad de negocio cuente con una cadena de mando clara para la gestión de riesgos y protección de datos.

## 1. Organigrama Funcional del Holding

```mermaid
graph TD
    %% Centro de Mando
    Holding((Holding OmniGroup))

    %% Nivel Directivo (Representación)
    Holding --- D1[Director OmniSalud]
    Holding --- D2[Director OmniBank]
    Holding --- D3[Director OmniRobotics]
    Holding --- D4[Director OmniRetail]

    %% Nivel Administrativo (Gestión)
    D1 --> A1[Administrador de Unidad]
    D2 --> A2[Administrador de Unidad]
    D3 --> A3[Administrador de Unidad]
    D4 --> A4[Administrador de Unidad]

    %% Nivel Operativo (Ejecución)
    A1 --> E1[4 Empleados Operativos]
    A2 --> E2[4 Empleados Operativos]
    A3 --> E3[4 Empleados Operativos]
    A4 --> E4[4 Empleados Operativos]

    %% Estilos Profesionales
    style Holding fill:#1a1a1a,stroke:#333,stroke-width:2px,color:#fff
    style D1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style D2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style D3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style D4 fill:#f5f5f5,stroke:#333,stroke-width:1px