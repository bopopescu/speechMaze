# Lecciones aprendidas, Esteban Santamaría Alfaro

- Aprendí a usar de forma muy sencilla el reconocimiento de voz de google
- Aprendimos que se tienen que dejar las funciones de la interfaz con acceso
  a las variables globales ya que la parte de voz corre en un hilo diferente y
  este no tiene acceso a las variables de la pantalla
- También, como lección decidimos implementar las funciones que actualizan
  la interfaz de como funciones separadas que solo editan lo que se le
  solicitan y una variable booleana “update” para que luego sea la misma
  interfaz la que se actualice a si misma y devuelva el estado de update a
  false.