# Migracion de GitHub Projects a Jira

Procedimiento compartido de Avenex. No es documentacion de clientes: mantenerlo
fuera de public/, los directorios docs de MkDocs y la navegacion de GitHub Pages.
Los exports, tickets privados, mapas reales y evidencias pertenecen al repositorio
privado del producto. Nunca incluir credenciales.

## Roles

- Product / BA / SM: seleccionar producto, definir epicas, workflow y alcance.
- Architect: revisar mapeo, dependencias y propiedad por repositorio.
- Developer: ejecutar operaciones idempotentes y guardar checkpoints privados.
- Tester: reconciliar campos y comprobar visualmente el tablero.
- Docs: mantener este procedimiento y separar evidencia interna de guias publicas.

Aplicar el estandar operativo de Codex. Migrar no implica aprobar funcionalidades,
cambiar versiones ni autorizar el borrado del origen.

## Inventario y credenciales

1. Confirmar organizacion, proyecto origen, producto y clave Jira destino.
2. Exportar todas las paginas: ID, tipo, titulo, descripcion, estado, area,
   producto, version, prioridad, evidencia y asignaciones.
3. Filtrar por producto. Revisar individualmente branding compartido y items sin
   producto; no importar el tablero completo del estudio por defecto.
4. Separar tickets locales aun no creados de los tickets realmente migrados.
5. Guardar snapshot privado y reconciliar seleccionados y excluidos.

Usar email y API token de Atlassian, no password de la cuenta. Guardar fuera de
Git. En Windows, un PSCredential exportado con Export-Clixml usa DPAPI: debe
descifrarse con el mismo usuario Windows y equipo. Copiarlo a otro perfil no basta.
Nunca imprimir el token ni Authorization. Verificar permisos sobre el tenant
autorizado antes de escribir.

GitHub GraphQL y REST tienen limites separados. Respetar HTTP 429 y Retry-After;
aplicar backoff. Ante una escritura incierta, buscar el identificador origen antes
de reintentar. No recrear a ciegas.

## Proyecto y campos

### Revisar antes de crear

1. Leer las instrucciones del repositorio producto, su plan de versiones y el
   estandar operativo compartido. Identificar nombre de producto, repositorio
   canonico y alcance; no asumir que el nombre de la carpeta es el del producto.
2. Consultar el usuario autenticado y sus permisos. Paginar la busqueda de
   proyectos Jira accesibles y comparar clave, nombre y metadatos del producto.
3. Si ya existe un proyecto correcto, reutilizarlo. Inspeccionar tipo, esquema,
   estados, campos, versiones, epicas, filtro y board antes de tocar nada.
4. Si no aparece, distinguir proyecto inexistente de falta de permisos o proyecto
   archivado. Ante ambiguedad, preguntar; no crear un duplicado como solucion.
5. Solo con autorizacion de alta, elegir una clave disponible y crear un proyecto
   software company-managed dedicado, con responsable confirmado. Si la clave
   pertenece a otro producto, no renombrarlo ni reutilizarlo.
6. Revisar si la creacion produjo un board. Reutilizar el correspondiente; crear
   un Kanban y filtro de ese proyecto solo cuando falten y haya permisos.
7. Comprobar que las transiciones cubren los estados deseados y que los tickets
   existentes no perderan estados, padres ni resoluciones al adaptar el workflow.
8. Registrar privadamente clave/ID de proyecto, board, esquema y mapeos. No asumir
   IDs fijos ni codificar los IDs de Race Control en otro proyecto.

Endpoints publicos utiles: GET /rest/api/3/myself, GET /rest/api/3/mypermissions,
GET /rest/api/3/project/search, POST /rest/api/3/project y GET/POST
/rest/agile/1.0/board. Consultar la documentacion vigente y los parametros
requeridos antes de ejecutar; no copiar plantillas o IDs sin validar el tenant.

Crear un proyecto software company-managed dedicado si se requiere este workflow.
No modificar otros proyectos ni sus esquemas. Descubrir IDs de campos, tipos,
estados y transiciones desde la API; no reutilizar IDs de otro tenant.

| Origen | Jira |
| --- | --- |
| Producto | Proyecto dedicado y etiqueta de producto |
| Draft de tarea | Task salvo clasificacion revisada |
| Funcionalidad | Epic mediante Parent |
| Area | Component, por ejemplo UX, Admin o Docs |
| Version objetivo | Fix version sin liberar hasta aprobacion explicita |
| Prioridad | Prioridad nativa con mapeo documentado |
| Evidencia | Etiqueta y metadatos originales |
| ID origen | Etiqueta unica y propiedad del ticket |
| Titulo original y campos | Snapshot privado y propiedad del ticket |

Estados: Backlog, To do, In Progress, In Game Testing, Review y Done. Los dos
primeros usan categoria To Do, los tres siguientes In Progress y Done usa Done.
En otros productos, acordar Testing en lugar de In Game Testing si corresponde.
No perder los estados de pruebas/revision por adaptar todo al tablero por defecto.
Revisar Resolution aparte: categoria Done no garantiza que ese campo este resuelto.

Asignar un esquema dedicado antes de importar en un proyecto vacio. Si ya contiene
tickets, usar el procedimiento soportado por Jira para migrar workflows.

## Epicas y titulos

Crear epicas por capacidad funcional o resultado coherente, no por prefijo antiguo
ni equipo. UX, runtime, admin y documentacion especifica de un modulo pertenecen a
la misma epica y mantienen sus areas y repositorios propietarios independientes.
Separar trabajo transversal de identidad visual, distribucion o infraestructura.

Los nombres deben ser completos y comprensibles. Usar siglas solo entre parentesis
cuando ayuden a reconocer el concepto. Por ejemplo: Control del sistema de
reduccion de resistencia aerodinamica (DRS), no solamente DRS.

Cada tarea tiene un unico Parent. Para dependencias entre modulos usar enlaces,
no duplicar tareas. Conservar propietario y tipo de cambio en cada ticket; separar
entregables independientes por repositorio cuando corresponda.

Quitar identificadores artificiales como DRS-T01 u OVL-T14 del resumen: Jira ya
asigna una clave. Mantener palabras de dominio que hagan entendible la accion,
incluso fuera del tablero. Guardar codigo y titulo anteriores en los metadatos y
mapa privado. No borrar contenido funcional por limpiar el prefijo.

Las nuevas epicas de agrupacion quedan en Backlog hasta revisar su estado de
planificacion. No cambiar estados ni versiones de los hijos. Una epica no queda
aprobada solo porque un hijo paso sus pruebas.

## Ejecucion y verificacion

1. Importar un piloto pequeno y comprobar todos los campos.
2. Usar un marcador estable por ticket y otro por epica. Buscar antes de crear;
   detenerse si existen multiples coincidencias.
3. Guardar metadatos originales junto a la creacion cuando sea posible.
4. Convertir descripciones a Atlassian Document Format sin perder texto. Markdown
   literal en parrafos conserva contenido pero no equivale a formato enriquecido.
5. Aplicar estados mediante transiciones disponibles y guardar el mapa tras cada cambio.
6. Asignar Parent y limpiar resumen sin reemplazar descripcion, etiquetas ni otros campos.
7. Releer todas las paginas del destino. Verificar IDs unicos, resumen esperado,
   descripcion, estado, prioridad, area, version, evidencia y Parent.
8. Comprobar que los identificadores antiguos siguen recuperables.
9. Informar por separado tickets importados, tickets locales nuevos y epicas nuevas.

Los drafts no tienen historial de comentarios de un issue de repositorio. Para
issues reales, inventariar comentarios, adjuntos, enlaces e historial y declarar
que se migro realmente; no asumir transferencia automatica.

Mantener GitHub intacto hasta autorizacion de archivo. Despues de renombrar,
verificar contra el mapa nuevo aprobado, no exigir el resumen antiguo ni contar
epicas como duplicados de tareas.

## Tablero y visibilidad

En Configure board > Columns, crear las seis columnas en orden y arrastrar cada
estado existente desde Unmapped statuses a su columna. Renombrar una columna no
cambia su asociacion. Distinguir el area opcional de Kanban backlog de una columna
visible adicional.

En Configure board > Layout > Card layout, agregar Parent a las tarjetas Kanban
si no muestran ya la epica. Algunas interfaces antiguas lo llaman Epic Link;
preferir Parent. Opcionalmente agrupar por Epics en Swimlanes. Las columnas siguen
siendo estados, no nombres de funcionalidades.

Abrir el tablero, inspeccionar tarjetas de dos epicas diferentes y comprobar que
se ve el nombre/clave del padre y se puede abrir. Revisar filtros, quick filters
y subconsultas de versiones si faltan tickets.

La API publica permite asignar Parent y consultar el tablero, pero no expone todas
las opciones visuales de escritura. Usar la interfaz autenticada para Card layout;
no inventar endpoints privados. Verificar Parent por API no demuestra su renderizado.
Sin acceso a navegador, informar que queda pendiente la comprobacion visual y
entregar los pasos anteriores al propietario.

## Versiones y roadmap

Usar Fix versions para versiones concretas, por ejemplo 0.1.1 o 0.2.0, no para
texto como P12 approval, Preview packaging o 0.2.0 (optional). Conservar esos
valores antiguos en los metadatos de migracion; representar opcionalidad con una
etiqueta o nota, no creando una segunda version casi identica.

Antes de asignar, leer el plan aprobado y los criterios de aceptacion. Distinguir
version actualmente implementada, objetivo futuro y estado de publicacion. Un
ticket Done puede pertenecer a una baseline aun no publicada. No marcar versiones
como released, fijar fechas ni incrementar la version del producto por organizar
el backlog.

Para una familia como 0.1.x, usar la siguiente version concreta solo si el alcance
esta identificado. Los recursos graficos y la documentacion de una funcionalidad
acompanan su objetivo, pero un rediseno pendiente no pertenece retroactivamente
a la baseline aprobada. Documentar las decisiones de asignacion nuevas.

Las epicas pueden tener varias Fix versions: usar la union de objetivos de los
hijos. Esto describe entregas parciales, no implica que toda la epica se libera
en cada version. Los trabajos internos sin version de aplicacion quedan sin
Fix version y con release-not-applicable; los objetivos aun no acordados deben
quedar pendientes de planificacion, no recibir una version inventada.

Releer los tickets tras escribir y comprobar versiones, estados, padres y campos
preservados. No borrar versiones heredadas durante la normalizacion: primero
verificar que no tengan otros consumidores y pedir autorizacion de limpieza.

## Prompt de relevo para otro proyecto

```text
Usa el rol Product / BA / SM y el estandar de migracion de avenex-docs.
Revisa las instrucciones y el roadmap del proyecto actual. Identifica su producto
y repositorio propietario. Busca su proyecto Jira, paginando y verificando permisos;
reutilizalo si existe. Si realmente no existe, crea un proyecto dedicado para este
producto y su board Kanban; confirma conmigo cualquier ambiguedad de nombre/clave.
No modifiques otros proyectos.

Inventaria los tickets origen y locales, selecciona solo los de este producto,
y conserva un snapshot privado. Propone o aplica las epicas por funcionalidad con
nombres completos; elimina prefijos artificiales de titulos conservando los IDs
anteriores. Mantiene propietarios y areas, y asigna versiones segun el plan aprobado.
No inventes objetivos para tareas sin plan ni publiques versiones.

Migra de manera idempotente, preserva el origen y verifica campo a campo. Configura
o indica los pasos de las columnas y Parent en las tarjetas. No declares completada
la comprobacion visual si no tienes navegador autenticado.

Entrega enlaces, conteos separados de tareas importadas/locales y epicas, mapa
privado, versiones y pendientes. No publiques datos internos ni hagas commits,
push o releases sin autorizacion separada.
```

Este prompt es una instruccion reutilizable; no instala automaticamente un slash
command. Completar el tenant y origen correctos mediante contexto verificado,
nunca pegando tokens en el prompt.

## Cierre

- Alcance reconciliado y proyectos ajenos intactos.
- Sin duplicados; identificadores anteriores recuperables.
- Todos los hijos asociados; estados, versiones y evidencia conservados.
- Estados mapeados y epica visible comprobada en tarjetas.
- Snapshots y mapa privado conservados fuera de la documentacion publica.
- Sin secretos ni rutas personales publicados.
- Resumen con cantidades, enlaces, limitaciones y pasos manuales pendientes.

## Referencias

- [Columnas](https://support.atlassian.com/jira-software-cloud/docs/configure-columns/)
- [Tarjetas](https://support.atlassian.com/jira-software-cloud/docs/customize-cards/)
- [Parent reemplaza Epic Link](https://support.atlassian.com/jira-software-cloud/docs/upcoming-changes-epic-link-replaced-with-parent/)
- [API Jira](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
