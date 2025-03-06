CREATE DATABASE IF NOT EXISTS 4thewords_prueba_kennett_ramirez;
USE 4thewords_prueba_kennett_ramirez;
INSERT INTO leyendas (
    nombre,
    categoria,
    descripcion,
    fecha,
    provincia,
    canton,
    distrito,
    imagen_url
  )
VALUES (
    'El Cadejos',
    'Magia',
    'La leyenda del Cadejos es una de las más conocidas en Costa Rica. Se trata de un perro gigante que aparece en la noche para proteger a los viajeros y borrachos.',
    '1970-01-01',
    'Cartago',
    'Cartago',
    'Llano Grande',
    'http://localhost:8080/static/bb750840-db66-4d44-af72-ca003c600cd5.jpg'
  ),
  (
    'La Cegua',
    'Magia',
    'La Cegua es un ser monstruoso que se aparece de noche por caminos solitarios a los hombres mujeriegos que viajan solos, generalmente a caballo (o en automóvil o motocicleta, en relatos más modernos), bajo la forma de una hermosa muchacha.',
    '1985-01-01',
    'Guanacaste',
    'Liberia',
    'Nacascolo',
    'http://localhost:8080/static/0b38cbf4-bd62-4822-bec1-66ccfdd8c7ad.jpeg'
  ),
  (
    'La Llorona',
    'Magia',
    'La leyenda de la Llorona cuenta la historia de una mujer que busca a sus hijos perdidos tras un trágico accidente. Se dice que su llanto desgarrador se puede escuchar en noches oscuras y cerca de ríos y bosques.',
    '1963-01-01',
    'San José',
    'Puriscal',
    'Mercedes Sur',
    'http://localhost:8080/static/38cf3b9d-3cf0-4429-8a43-1b9eb88b4068.jpg'
  ),
  (
    'Leyenda de la Roca Bruja',
    'Topográfica',
    'Dice la leyenda que los indios que habitan en ese lugar eran atacados por una bruja constantemente, se robaba a los niños y se los comía.',
    '1988-06-06',
    'Guanacaste',
    'La Cruz',
    'La Cruz',
    'http://localhost:8080/static/412d025d-7ca0-4a34-a990-fff02b063877.jpg'
  ),
  (
    'La Virgen del Mar',
    'Religiosa',
    'En 1913, la embarcación El Galileo naufragó mar adentro en Puntarenas y su tripulación fue rescatada. Al llegar a tierra, los marineros contaron que una mujer los visitó para darles fortaleza y comida, fue por eso, según ellos, que sobrevivieron.',
    '1913-06-01',
    'Puntarenas',
    'Puntarenas',
    'Puntarenas',
    'http://localhost:8080/static/03e57259-f0fb-42f4-95f8-87c95770eafc.jpeg'
  ),
  (
    'La Carreta sin Bueyes',
    'Magia',
    'La leyenda habla acerca del espectro nocturno de una carreta que aparece por las noches y recorre las calles de algún pueblo o ciudad, sin que se vean bueyes que la arrastren ni tampoco boyeros que la dirijan.',
    '1977-06-24',
    'San José',
    'Escazú',
    'Escazú',
    'http://localhost:8080/static/98ae0d02-f285-4357-9e35-f68ab9305fde.jpg'
  ),
  (
    'La Virgen de Ujarrás',
    'Religiosa',
    'Dice la leyenda que un indígena estaba pescando a la vera del río secundario Madre de Dios. En tal actividad se encontraba, cuando se distrajo por una caja de madera que flotaba y que contenía una imagen de la Virgen María.',
    '1835-04-16',
    'Cartago',
    'Cartago',
    'Aguacaliente',
    'http://localhost:8080/static/449fd3d8-e563-44e8-a03d-b33d6d7c968d.jpg'
  ),
  (
    'El Tesoro de la Isla del Coco',
    'Topográfica',
    'La leyenda del tesoro de la Isla del Coco en Costa Rica se refiere a un botín de oro y plata que supuestamente fue robado y escondido en la isla',
    '1869-05-11',
    'Puntarenas',
    'Puntarenas',
    'Puntarenas',
    'http://localhost:8080/static/b5cd23d6-c1e7-43a7-a212-0029f218d24b.jpg'
  ),
  (
    'La Bruja de Escazú',
    'Magia',
    'Cuenta la leyenda que esta bruja era negrita y una de las últimas brujas del pueblo más renombradas, que habitaba al norte de la Iglesia del centro de Escazú.',
    '1961-03-15',
    'San José',
    'Escazú',
    'Escazú',
    'http://localhost:8080/static/bc0b2394-cab5-4df0-bf9a-20d98407d2cd.jpg'
  ),
  (
    'La Bruja de Zárate',
    'Magia',
    'La leyenda dice que una bruja se enamoró del gobernador español de la ciudad Zárate, pero al ser rechazada por él, transformó al pueblo entero en esta gran piedra y a sus pobladores en animales, incluyendo al gobernador en un pavo real.',
    '1930-08-13',
    'San José',
    'Aserrí',
    'Aserrí',
    'http://localhost:8080/static/0e73d2a7-a246-43a2-bb0e-d00d2d20e81f.jpg'
  );