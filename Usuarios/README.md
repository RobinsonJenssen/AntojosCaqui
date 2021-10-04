# Aplicación Usuarios

Con la aplicación usuarios se planea administrar las cuentas de usuarios creadas en la herramienta. Para lograr, con facilidad, esto se está usando la clase `get_user_model` proporcionada por el *framework Django*.

## Clase `DocumentType`
Partiendo de la normalización del modelo se obtuvo la clase `DocumentType` la cual se encarga de guardar los tipos de documentos de identidad y descripciones para cada uno.

## Clase `Profile`
Guardará información extra relacionada con la cuenta de usuario, como sería el nombre completo el tipo de documento y su número, un correo electrónico y finalmente un número de teléfono móvil.

## Clases `Country`, `State` y `City`
Partiendo de la normalización del modelo se obtuvieron las clases `Country`, `State` y `City`; las cuales son complementarias a la clase `Address`. Una vez se conozca una ciudad válida (en el modelo de negocio) a la cual se envía el pedido se podría establecer la dirección del inmueble. Asimismo, es posible establecer un huespeded distinto al quien realiza la compra.

## Clase `Address`
Guardará las direcciones de entrega que necesite guardar el cliente.
