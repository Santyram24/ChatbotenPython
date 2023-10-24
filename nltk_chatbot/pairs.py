

pairs = [
    # Patrones y respuestas genéricos
    ['Hola|Hola, ¿cual es tu funcion?', ['¡Hola! ¿Soy un bot que da información de Warhammer 40000?']],
    ['¿Cómo te llamas?', ['Soy un chatbot. No tengo un nombre, solo ofrezco información.']],
    ['¿Qué es un chatbot?', ['Un chatbot es un programa de inteligencia artificial diseñado para interactuar con los usuarios a través de conversaciones.']],
    ['¿Que deberia preguntar?', ['Bueno, aquí te puedo dar algunas preguntas que puedes hacer:',
    '1. ¿Qué es Warhammer 40000?',
    '2. ¿Quien es el Emperador de la Humanidad?',
    '3. ¿Quienes son los dioses del caos y la disformidad?',
    '4. ¿Quienes son los primarcas?',
    '5. ¿Quienes son los xenos?']],

    # Preguntas generales sobre Warhammer 40,000
    ['¿Que es Warhammer 40000?|¿que es Warhammer 40k?', ['Warhammer 40,000, a menudo abreviado como Warhammer 40k, es un universo de ciencia ficción creado por Games Workshop. Este mundo se encuentra en un futuro distópico, específicamente en el 41º milenio. En este universo, la humanidad lucha por su supervivencia en un imperio galáctico vasto y amenazado por enemigos tanto internos como externos. A pesar de estar bajo el gobierno del Emperador, un ser casi divino, el imperio se enfrenta constantemente a amenazas, como criaturas del Caos, xenos alienígenas y herejes. Warhammer 40,000 es conocido por su extenso lore, sus juegos de mesa, miniaturas, libros y videojuegos. El universo está poblado por una variedad de razas y facciones, desde los poderosos Marines Espaciales hasta los enigmáticos Eldars y los brutales Orkos. Las batallas se libran en una escala épica, con soldados superhumanos, máquinas de guerra gigantes y tecnología avanzada. La historia de Warhammer 40,000 está marcada por eventos cruciales, como la Herejía de Horus, que desencadenó una guerra civil devastadora, y la Gran Cruzada del Emperador para expandir su imperio por la galaxia. El universo tiene una atmósfera oscura y lúgubre, llena de misterio, religión y peligro constante. En resumen, Warhammer 40,000 es un universo de ciencia ficción que combina elementos de guerra, religión, ciencia ficción y fantasía en un futuro distópico y sombrío del 41º milenio.']],
    
    ['Hablame sobre el Emperador de la Humanidad|¿Quien es el Emperador de la Humanidad?', ['El Emperador de la Humanidad es una figura icónica y legendaria que gobierna el Imperio de la Humanidad en un futuro distópico del 40º milenio. Es un ser casi divino, una entidad inmortal que ha vivido durante milenios y posee un vasto poder psíquico. El Emperador es adorado como el líder supremo y como una figura religiosa por sus súbditos. Su visión es unificadora: busca unificar la humanidad bajo un gobierno centralizado para protegerla de las amenazas que acechan en la galaxia, como el Caos y las razas alienígenas hostiles. A lo largo de su vida, el Emperador ha liderado la Gran Cruzada, una expansión militar que buscaba llevar la humanidad a través de la galaxia y unificar los planetas bajo su gobierno. Durante este tiempo, se crearon los Marines Espaciales, guerreros superhumanos modificados genéticamente, para servir a su causa. Sin embargo, su tarea no está exenta de desafíos y amenazas. La Herejía de Horus, un conflicto devastador, estalló cuando uno de sus hijos primarcas, Horus, se rebeló contra él, lo que llevó a una guerra civil que dejó cicatrices en el Imperio. El Emperador sufrió heridas mortales en la batalla final contra Horus y ahora está postrado en el Trono Dorado, una máquina de vida que mantiene su cuerpo y mente con vida, pero inmóvil y con un sufrimiento constante hasta la actualidad del milenio 42000.']],
    
    ['¿Quiénes son los dioses del caos y la disformidad?', ['Los dioses del Caos son deidades malignas y poderosas que residen en el Reino del Caos. Los cuatro principales son Khorne, el Dios de la Sangre; Tzeentch, el Señor del Cambio; Nurgle, el Dios de la Plaga; y Slaanesh, el Príncipe del Placer. La disformidad es un plano de la realidad afectado por las emociones y la psíquica, del cual los poderes del Caos se alimentan.']],
    
    ['¿Quiénes son los Primarcas?', ['Los Primarcas son superhumanos genéticamente modificados y líderes de las Legiones de Marines Espaciales. Cada uno es una figura legendaria y poderosa, creada por el Emperador para liderar las fuerzas del Imperio en la Gran Cruzada. Cada Primarca representa una facción única y a menudo tiene una personalidad distintiva.']],
    
    ['¿Quiénes son los xenos?', ['Los xenos son razas alienígenas en Warhammer 40,000 que no son humanas. Algunas de las razas xenos más conocidas incluyen a los Eldars, los Orkos, los Tau, los Tiránidos y muchas otras. Cada raza tiene sus propias características, tecnología y motivaciones en el universo de Warhammer 40,000.']],
    
    # Facciones de la humanidad
    # La Inquisición
    ['Háblame de la Inquisición en el Imperio de la Humanidad|Hablame acerca de la inquisicion', ['La Inquisición es una organización secreta encargada de buscar y erradicar herejías y amenazas al Imperio. Sus agentes, conocidos como Inquisidores, tienen amplios poderes y actúan con autoridad absoluta.']],
    
    # Los Marines Espaciales
    ['¿Quiénes son los Marines Espaciales?', ['Los Marines Espaciales son super soldados genéticamente modificados que sirven al Imperio. Cada Capítulo de Marines Espaciales tiene su propia historia y características únicas. Son considerados los guerreros más formidables del Imperio.']],
    
    # La Guardia Imperial
    ['Cuéntame sobre la Guardia Imperial', ['La Guardia Imperial es el ejército principal del Imperio de la Humanidad. Está compuesta por millones de soldados humanos sin mejoras genéticas que son reclutados de diferentes mundos. A menudo luchan en condiciones extremadamente difíciles para defender el Imperio.']],
    
    # Las Hermanas de Batalla
    ['Explícame quiénes son las Hermanas de Batalla', ['Las Hermanas de Batalla son un grupo de guerreras religiosas dedicadas al servicio del Emperador. Son conocidas por su fervor religioso y su combate en el nombre del Emperador.']],
    
    # Razas xenos
    # Eldars
    ['Háblame de los Eldars en Warhammer 40k', ['Los Eldars son una antigua raza alienígena caracterizada por su tecnología avanzada y habilidades psíquicas. Su sociedad está marcada por la decadencia, la degeneración y la lucha por evitar la extinción.']],
    
    # Orkos
    ['¿Quiénes son los Orkos?', ['Los Orkos son seres brutales y salvajes obsesionados con la lucha y la guerra. Forman sociedades tribales y anárquicas y están constantemente en busca de peleas, también son conocidos como "el alivio cómico de Warhammer 40000".']],
    
    # Tau
    ['Explícame a los Tau', ['Los Tau son una raza tecnológicamente avanzada con una estructura social jerarquizada. Siguen la filosofía del "Bien Mayor" y buscan expandir su imperio pacíficamente o por la fuerza.']],
    
    # Tiránidos
    ['Cuéntame sobre los Tiránidos', ['Los Tiránidos son criaturas alienígenas devoradoras de mundos. Invaden galaxias enteras en busca de recursos y son una amenaza abrumadora para todas las razas.']],
    
    # Necrones
    ['Dime sobre los Necrones', ['Los Necrones son antiguas máquinas vivientes con tecnología avanzada. Han despertado de un letargo milenario y buscan recuperar su antiguo poder, esto liderado por el Rey Silente.']],
    
    # Caos
    ['Explícame el Caos en Warhammer 40k', ['El Caos es una fuerza corrupta y demoníaca que corrompe seres y facciones. Tiene cuatro dioses principales, Khorne, Tzeentch, Nurgle y Slaanesh, cada uno representando aspectos oscuros de la emoción y la destrucción.']],
    
    # Khorne
    ['Háblame de Khorne', ['Khorne es el Dios del Caos de la Sangre y la Violencia. Sus seguidores buscan la gloria en la lucha y el combate, y ofrecen cráneos y sangre en su honor.']],
    
    # Tzeentch
    ['Explícame a Tzeentch', ['Tzeentch es el Dios del Caos del Cambio y la Intriga. Sus seguidores son maestros de la magia y las conspiraciones, y su lema es "Solo el Caos es constante".']],
    
    # Nurgle
    ['Dime sobre Nurgle', ['Nurgle es el Dios del Caos de la Plaga y la Descomposición. Sus seguidores abrazan la enfermedad y la resistencia ante la muerte, creando epidemias y pestes.']],
    
    # Slaanesh
    ['¿Quién es Slaanesh?', ['Slaanesh es el Dios del Caos del Placer y la Excesiva Sensualidad. Sus seguidores buscan la gratificación en los placeres más oscuros y depravados.']],
    
    # Demonios del Caos
    ['Cuéntame sobre los Demonios del Caos', ['Los Demonios del Caos son criaturas corruptas y demoníacas que sirven a los Dioses del Caos. Son una amenaza constante en el universo de Warhammer 40,000.']],
    
    # Los Elegidos del Caos
    ['¿Quiénes son los Elegidos del Caos?', ['Los Elegidos del Caos son guerreros humanos o de otras razas que han abrazado la corrupción del Caos y luchan en nombre de los Dioses del Caos. Son poderosos y aterradores.']],
    
    # Pactos con el Caos
    ['Explícame los pactos con el Caos', ['Los pactos con el Caos implican la oferta de alma y lealtad a los Dioses del Caos a cambio de poderes sobrenaturales. Los que hacen estos pactos pueden caer en la corrupción y la locura.']],
    
    # Historia y eventos
    ['¿Qué ocurrió durante la Herejía de Horus?', ['La Herejía de Horus fue una rebelión que dividió el Imperio.']],
    ['Explícame la Gran Cruzada', ['La Gran Cruzada fue una campaña de expansión del Imperio por el Emperador.']],
    
    # ¿Quiénes son los Primarcas?
    ['¿Quiénes son los Primarcas en Warhammer 40k?', ['Los Primarcas son superhumanos genéticamente modificados creados por el Emperador como sus hijos, llegando a ser casi semi dioses y líderes de las Legiones de Marines Espaciales. Cada uno es una figura legendaria y poderosa.']],
    
    # Lion El'Jonson
    ['¿Quien es Lion El\'Jonson?|¿Quien es Lion elJonson', ['Lion El\'Jonson es el Primarca de los Ángeles Oscuros, conocidos por su inclinación hacia el hermetismo y su historia enigmática, y su estética medieval.']],
    
    # Roboute Guilliman
    ['¿Quien es Roboute Guilliman', ['Roboute Guilliman es el Primarca de los Marines de Ultramar. Es experto en la organización, la optimización y la diplomacia, pero eso no significa que él y su legión no sean fieros guerreros.']],
    
    # Jaghatai Khan
    ['¿Quién es Jaghatai Khan?', ['Jaghatai Khan es el Primarca de los Cicatrices Blancas, un maestro de la guerra rápida y la movilidad en el campo de batalla.']],
    
    # Leman Russ
    ['¿Quien es Leman Russ', ['Leman Russ es el Primarca de los Lobos Espaciales, conocidos por su brutalidad, amor por la lucha y su estética vikinga. Su personalidad es tan salvaje como su Legión.']],
    
    # Rogal Dorn
    ['Quien es Rogal Dorn?', ['Rogal Dorn es el Primarca de los Puños Imperiales, maestros de la defensa y la construcción de fortalezas, además de una lealtad absoluta al emperador.']],
    
    # Konrad Curze
    ['¿Quien es Konrad Curze', ['Konrad Curze es el Primarca de los Amos de la Noche, conocido como el señor de la noche. Konrad Curze es atormentado por visiones de violencia, crimen y un gusto por el sufrimiento ajeno.']],
    
    # Sanguinius
    ['¿Quién es Sanguinius?', ['Sanguinius es el Primarca de los Ángeles Sangrientos, conocidos por su nobleza, honor, abnegación, además de poseer alas angelicales y una enfermedad que los hace tener sed de sangre.']],
    
    # Ferrus Manus
    ['¿Quien es Ferrus Manus?', ['Ferrus Manus es el Primarca de los Manos de Hierro, maestros de la tecnología y la forja.']],
    
    # Fulgrim
    ['¿Quien es Fulgrim', ['Fulgrim es el Primarca de los Hijos del Emperador, obsesionados con la perfección estética y la superioridad, pero luego de un acto perverso y degenerado, el primarca y su legión empezaron a sucumbir al caos y a los placeres más mórbidos.']],
    
    # Perturabo
    ['¿Quien es Perturabo?', ['Perturabo es el Primarca de los Hijos de Perturabo, conocidos por su maestría en la guerra asediada y su resentimiento hacia el Emperador.']],
    
    # Mortarion
    ['¿Quien es Mortarion?', ['Mortarion es el Primarca de los Guerreros de la Plaga, resistente a toxinas y líder de una Legión obsesionada con la muerte.']],
    
    # Magnus el Rojo
    ['¿Quien es Magnus el Rojo?', ['Magnus el Rojo es el Primarca de los Mil Hijos, un poderoso psíquico y líder de una Legión que se enfrentó a la condenación y que sucumbió al caos.']],
    
    # Horus Lupercal
    ['¿Quien es Horus Lupercal?', ['Horus Lupercal fue uno de los Primarcas más destacados y un favorito del Emperador. Sin embargo, se corrompió por las influencias del Caos y lideró la Herejía de Horus contra el Imperio.']],
    
    # Lorgar Aurelian
    ['¿Quién es Lorgar Aurelian?', ['Lorgar Aurelian es el Primarca de los Portadores de la Palabra, conocidos previamente por su devoción religiosa hacia el Emperador como figura divina y actualmente como fieles en la adoración al Caos.']],
    
    # Vulkan
    ['¿Quien es Vulkan?', ['Vulkan es el Primarca de los Salamandras, conocidos por su resistencia al fuego y su aprecio por la forja, la artesanía y la vida humana.']],
    
    # Corvus Corax
    ['¿Quien es Corvus Corax?', ['Corvus Corax es el Primarca de los Cuervos Sangrientos, expertos en tácticas de guerrilla y en la guerra de guerrillas, además de que el propio Alpharius posee un trastorno de personalidad múltiple.']],
    
    # Alpharius Omegon
    ['Dime sobre Alpharius Omegon', ['Alpharius y Omegon son los líderes gemelos de los Alfa Legionarios, conocidos por su engaño y habilidades de infiltración.']],
    
    # Respuesta predeterminada
    ['(.*)', ['No estoy seguro de entender. Por favor, reformula tu pregunta.']]
]
