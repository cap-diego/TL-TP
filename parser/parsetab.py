
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'columna comilla corchete_abre corchete_cierra empate enroque_1 enroque_2 equis espacio fila gano_blanco gano_negro jaque jaque_mate llave_abre llave_cierra numero palabra parentecis_abre parentecis_cierra pieza puntoS : METADATA JUGADASMETADATA : ITEM_METADATA METADATA\n                | lambdaITEM_METADATA : corchete_abre palabra comilla palabra comilla corchete_cierraJUGADAS  : JUGADA JUGADAS\n                | MOVIMIENTO_FINALMOVIMIENTO_FINAL :   gano_blanco\n                        |   gano_negro\n                        |   empateJUGADA   :   NUMERO_JUGADA punto COMENTARIO MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO\n                |   NUMERO_JUGADA punto COMENTARIO MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO\n                |   NUMERO_JUGADA punto COMENTARIO MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO\n                |   NUMERO_JUGADA punto COMENTARIO MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO \n                |   NUMERO_JUGADA punto MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO\n                |   NUMERO_JUGADA punto MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO\n                |   NUMERO_JUGADA punto MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO\n                |   NUMERO_JUGADA punto MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTONUMERO_JUGADA  :   numeroNUMERO_JUGADA_OPCIONAL   :   NUMERO_JUGADA punto punto punto COMENTARIO\n                                |   NUMERO_JUGADA punto punto punto\n                                |   lambdaMOVIMIENTO   :   PIEZA POS_OPCIONAL equis PIEZA POS ESPECIAL\n                    |   PIEZA POS_OPCIONAL PIEZA POS ESPECIAL\n                    |   PIEZA equis POS ESPECIAL\n                    |   PIEZA POS ESPECIAL\n                    |   enroque_1 ESPECIAL\n                    |   enroque_2 ESPECIALPOS_OPCIONAL :   columna fila\n                    |   columna\n                    |   filaPOS    :   columna filaESPECIAL :   jaque_mate\n                |   jaque\n                |   lambdaPIEZA    :   pieza\n                |   lambdaCOMENTARIO   :   llave_abre COM llave_cierra\n                    |   parentecis_abre COM parentecis_cierra\n                    |   llave_abre llave_cierra\n                    |   parentecis_abre parentecis_cierraCOM  :   COMENTARIO_REAL COM \n            |   MOVIMIENTO_OPCIONAL COM\n            |   COMENTARIO COM\n            |   COMENTARIO_REAL\n            |   MOVIMIENTO_OPCIONAL \n            |   COMENTARIOCOMENTARIO_REAL      :   palabra espacio COMENTARIO_REAL\n                            |   palabraMOVIMIENTO_OPCIONAL  :   NUMERO_OPCIONAL MOVIMIENTONUMERO_OPCIONAL  :   NUMERO_JUGADA PUNTOS_OPCIONALESPUNTOS_OPCIONALES    :   punto\n                            |   punto punto punto\n                            |   lambdalambda :'
    
_lr_action_items = {'corchete_abre':([0,3,76,],[5,5,-4,]),'gano_blanco':([0,2,3,4,7,14,24,25,35,43,46,49,50,51,52,53,59,60,69,72,74,75,76,78,80,81,84,86,87,88,89,91,93,94,95,97,],[-54,10,-54,-3,10,-2,-54,-54,-39,-40,-54,-26,-32,-33,-34,-27,-17,-37,-38,-54,-25,-31,-4,-13,-15,-16,-54,-24,-31,-11,-12,-14,-23,-54,-10,-22,]),'gano_negro':([0,2,3,4,7,14,24,25,35,43,46,49,50,51,52,53,59,60,69,72,74,75,76,78,80,81,84,86,87,88,89,91,93,94,95,97,],[-54,11,-54,-3,11,-2,-54,-54,-39,-40,-54,-26,-32,-33,-34,-27,-17,-37,-38,-54,-25,-31,-4,-13,-15,-16,-54,-24,-31,-11,-12,-14,-23,-54,-10,-22,]),'empate':([0,2,3,4,7,14,24,25,35,43,46,49,50,51,52,53,59,60,69,72,74,75,76,78,80,81,84,86,87,88,89,91,93,94,95,97,],[-54,12,-54,-3,12,-2,-54,-54,-39,-40,-54,-26,-32,-33,-34,-27,-17,-37,-38,-54,-25,-31,-4,-13,-15,-16,-54,-24,-31,-11,-12,-14,-23,-54,-10,-22,]),'numero':([0,2,3,4,7,14,20,21,22,24,25,29,31,35,36,37,38,39,43,46,49,50,51,52,53,55,59,60,65,69,72,74,75,76,78,80,81,82,84,86,87,88,89,91,93,94,95,97,],[-54,13,-54,-3,13,-2,13,13,13,-54,-54,13,13,-39,13,13,13,-48,-40,-54,-26,-32,-33,-34,-27,13,-17,-37,-49,-38,-54,-25,-31,-4,-13,-15,-16,-47,-54,-24,-31,-11,-12,-14,-23,-54,-10,-22,]),'$end':([1,6,8,10,11,12,16,],[0,-1,-6,-7,-8,-9,-5,]),'palabra':([5,18,21,22,24,25,35,36,37,38,39,43,46,49,50,51,52,53,60,64,65,69,72,74,75,82,84,86,87,93,94,97,],[15,28,39,39,-54,-54,-39,39,39,39,-48,-40,-54,-26,-32,-33,-34,-27,-37,39,-49,-38,-54,-25,-31,-47,-54,-24,-31,-23,-54,-22,]),'punto':([9,13,30,41,57,67,79,83,],[17,-18,57,67,79,83,90,92,]),'enroque_1':([13,17,19,20,24,25,29,31,32,33,35,40,41,43,46,49,50,51,52,53,55,56,58,60,66,67,68,69,72,74,75,77,84,86,87,90,92,93,94,96,97,],[-18,24,24,-54,-54,-54,-54,-54,24,-21,-39,24,-54,-40,-54,-26,-32,-33,-34,-27,-54,24,24,-37,-50,-51,-53,-38,-54,-25,-31,24,-54,-24,-31,-20,-52,-23,-54,-19,-22,]),'enroque_2':([13,17,19,20,24,25,29,31,32,33,35,40,41,43,46,49,50,51,52,53,55,56,58,60,66,67,68,69,72,74,75,77,84,86,87,90,92,93,94,96,97,],[-18,25,25,-54,-54,-54,-54,-54,25,-21,-39,25,-54,-40,-54,-26,-32,-33,-34,-27,-54,25,25,-37,-50,-51,-53,-38,-54,-25,-31,25,-54,-24,-31,-20,-52,-23,-54,-19,-22,]),'pieza':([13,17,19,20,24,25,29,31,32,33,35,40,41,43,44,46,47,48,49,50,51,52,53,55,56,58,60,66,67,68,69,71,72,74,75,77,84,86,87,90,92,93,94,96,97,],[-18,26,26,-54,-54,-54,-54,-54,26,-21,-39,26,-54,-40,26,-54,-29,-30,-26,-32,-33,-34,-27,-54,26,26,-37,-50,-51,-53,-38,26,-54,-25,-28,26,-54,-24,-31,-20,-52,-23,-54,-19,-22,]),'equis':([13,17,19,20,23,24,25,26,27,29,31,32,33,35,40,41,43,44,46,47,48,49,50,51,52,53,55,56,58,60,66,67,68,69,72,74,75,77,84,86,87,90,92,93,94,96,97,],[-18,-54,-54,-54,45,-54,-54,-35,-36,-54,-54,-54,-21,-39,-54,-54,-40,71,-54,-29,-30,-26,-32,-33,-34,-27,-54,-54,-54,-37,-50,-51,-53,-38,-54,-25,-28,-54,-54,-24,-31,-20,-52,-23,-54,-19,-22,]),'columna':([13,17,19,20,23,24,25,26,27,29,31,32,33,35,40,41,43,44,45,46,47,48,49,50,51,52,53,55,56,58,60,66,67,68,69,70,71,72,74,75,77,84,85,86,87,90,92,93,94,96,97,],[-18,-54,-54,-54,47,-54,-54,-35,-36,-54,-54,-54,-21,-39,-54,-54,-40,-54,73,-54,-29,-30,-26,-32,-33,-34,-27,-54,-54,-54,-37,-50,-51,-53,-38,73,-54,-54,-25,-28,-54,-54,73,-24,-31,-20,-52,-23,-54,-19,-22,]),'fila':([13,17,19,20,23,24,25,26,27,29,31,32,33,35,40,41,43,46,47,49,50,51,52,53,55,56,58,60,66,67,68,69,72,73,74,75,77,84,86,87,90,92,93,94,96,97,],[-18,-54,-54,-54,48,-54,-54,-35,-36,-54,-54,-54,-21,-39,-54,-54,-40,-54,75,-26,-32,-33,-34,-27,-54,-54,-54,-37,-50,-51,-53,-38,-54,87,-25,-31,-54,-54,-24,-31,-20,-52,-23,-54,-19,-22,]),'comilla':([15,28,],[18,54,]),'llave_abre':([17,20,21,22,24,25,29,35,36,37,38,39,43,46,49,50,51,52,53,59,60,65,69,72,74,75,78,80,82,84,86,87,88,90,93,94,97,],[21,21,21,21,-54,-54,21,-39,21,21,21,-48,-40,-54,-26,-32,-33,-34,-27,21,-37,-49,-38,-54,-25,-31,21,21,-47,-54,-24,-31,21,21,-23,-54,-22,]),'parentecis_abre':([17,20,21,22,24,25,29,35,36,37,38,39,43,46,49,50,51,52,53,59,60,65,69,72,74,75,78,80,82,84,86,87,88,90,93,94,97,],[22,22,22,22,-54,-54,22,-39,22,22,22,-48,-40,-54,-26,-32,-33,-34,-27,22,-37,-49,-38,-54,-25,-31,22,22,-47,-54,-24,-31,22,22,-23,-54,-22,]),'llave_cierra':([21,24,25,34,35,36,37,38,39,43,46,49,50,51,52,53,60,61,62,63,65,69,72,74,75,82,84,86,87,93,94,97,],[35,-54,-54,60,-39,-44,-45,-46,-48,-40,-54,-26,-32,-33,-34,-27,-37,-41,-42,-43,-49,-38,-54,-25,-31,-47,-54,-24,-31,-23,-54,-22,]),'parentecis_cierra':([22,24,25,35,36,37,38,39,42,43,46,49,50,51,52,53,60,61,62,63,65,69,72,74,75,82,84,86,87,93,94,97,],[43,-54,-54,-39,-44,-45,-46,-48,69,-40,-54,-26,-32,-33,-34,-27,-37,-41,-42,-43,-49,-38,-54,-25,-31,-47,-54,-24,-31,-23,-54,-22,]),'jaque_mate':([24,25,46,72,75,84,87,94,],[50,50,50,50,-31,50,-31,50,]),'jaque':([24,25,46,72,75,84,87,94,],[51,51,51,51,-31,51,-31,51,]),'espacio':([39,],[64,]),'corchete_cierra':([54,],[76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'METADATA':([0,3,],[2,14,]),'ITEM_METADATA':([0,3,],[3,3,]),'lambda':([0,3,17,19,20,24,25,29,31,32,40,41,44,46,55,56,58,71,72,77,84,94,],[4,4,27,27,33,52,52,33,33,27,27,68,27,52,33,27,27,27,52,27,52,52,]),'JUGADAS':([2,7,],[6,16,]),'JUGADA':([2,7,],[7,7,]),'MOVIMIENTO_FINAL':([2,7,],[8,8,]),'NUMERO_JUGADA':([2,7,20,21,22,29,31,36,37,38,55,],[9,9,30,41,41,30,30,41,41,41,30,]),'COMENTARIO':([17,20,21,22,29,36,37,38,59,78,80,88,90,],[19,31,38,38,55,38,38,38,81,89,91,95,96,]),'MOVIMIENTO':([17,19,32,40,56,58,77,],[20,29,59,65,78,80,88,]),'PIEZA':([17,19,32,40,44,56,58,71,77,],[23,23,23,23,70,23,23,85,23,]),'NUMERO_JUGADA_OPCIONAL':([20,29,31,55,],[32,56,58,77,]),'COM':([21,22,36,37,38,],[34,42,61,62,63,]),'COMENTARIO_REAL':([21,22,36,37,38,64,],[36,36,36,36,36,82,]),'MOVIMIENTO_OPCIONAL':([21,22,36,37,38,],[37,37,37,37,37,]),'NUMERO_OPCIONAL':([21,22,36,37,38,],[40,40,40,40,40,]),'POS_OPCIONAL':([23,],[44,]),'POS':([23,45,70,85,],[46,72,84,94,]),'ESPECIAL':([24,25,46,72,84,94,],[49,53,74,86,93,97,]),'PUNTOS_OPCIONALES':([41,],[66,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> METADATA JUGADAS','S',2,'p_start','parser.py',7),
  ('METADATA -> ITEM_METADATA METADATA','METADATA',2,'p_metadata','parser.py',11),
  ('METADATA -> lambda','METADATA',1,'p_metadata','parser.py',12),
  ('ITEM_METADATA -> corchete_abre palabra comilla palabra comilla corchete_cierra','ITEM_METADATA',6,'p_item_metadata','parser.py',16),
  ('JUGADAS -> JUGADA JUGADAS','JUGADAS',2,'p_jugadas','parser.py',20),
  ('JUGADAS -> MOVIMIENTO_FINAL','JUGADAS',1,'p_jugadas','parser.py',21),
  ('MOVIMIENTO_FINAL -> gano_blanco','MOVIMIENTO_FINAL',1,'p_movimiento_final','parser.py',25),
  ('MOVIMIENTO_FINAL -> gano_negro','MOVIMIENTO_FINAL',1,'p_movimiento_final','parser.py',26),
  ('MOVIMIENTO_FINAL -> empate','MOVIMIENTO_FINAL',1,'p_movimiento_final','parser.py',27),
  ('JUGADA -> NUMERO_JUGADA punto COMENTARIO MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO','JUGADA',8,'p_jugada','parser.py',31),
  ('JUGADA -> NUMERO_JUGADA punto COMENTARIO MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO','JUGADA',7,'p_jugada','parser.py',32),
  ('JUGADA -> NUMERO_JUGADA punto COMENTARIO MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO','JUGADA',7,'p_jugada','parser.py',33),
  ('JUGADA -> NUMERO_JUGADA punto COMENTARIO MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO','JUGADA',6,'p_jugada','parser.py',34),
  ('JUGADA -> NUMERO_JUGADA punto MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO','JUGADA',7,'p_jugada','parser.py',35),
  ('JUGADA -> NUMERO_JUGADA punto MOVIMIENTO COMENTARIO NUMERO_JUGADA_OPCIONAL MOVIMIENTO','JUGADA',6,'p_jugada','parser.py',36),
  ('JUGADA -> NUMERO_JUGADA punto MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO COMENTARIO','JUGADA',6,'p_jugada','parser.py',37),
  ('JUGADA -> NUMERO_JUGADA punto MOVIMIENTO NUMERO_JUGADA_OPCIONAL MOVIMIENTO','JUGADA',5,'p_jugada','parser.py',38),
  ('NUMERO_JUGADA -> numero','NUMERO_JUGADA',1,'p_numero_jugada','parser.py',42),
  ('NUMERO_JUGADA_OPCIONAL -> NUMERO_JUGADA punto punto punto COMENTARIO','NUMERO_JUGADA_OPCIONAL',5,'p_numero_jugada_opcional','parser.py',46),
  ('NUMERO_JUGADA_OPCIONAL -> NUMERO_JUGADA punto punto punto','NUMERO_JUGADA_OPCIONAL',4,'p_numero_jugada_opcional','parser.py',47),
  ('NUMERO_JUGADA_OPCIONAL -> lambda','NUMERO_JUGADA_OPCIONAL',1,'p_numero_jugada_opcional','parser.py',48),
  ('MOVIMIENTO -> PIEZA POS_OPCIONAL equis PIEZA POS ESPECIAL','MOVIMIENTO',6,'p_movimiento','parser.py',52),
  ('MOVIMIENTO -> PIEZA POS_OPCIONAL PIEZA POS ESPECIAL','MOVIMIENTO',5,'p_movimiento','parser.py',53),
  ('MOVIMIENTO -> PIEZA equis POS ESPECIAL','MOVIMIENTO',4,'p_movimiento','parser.py',54),
  ('MOVIMIENTO -> PIEZA POS ESPECIAL','MOVIMIENTO',3,'p_movimiento','parser.py',55),
  ('MOVIMIENTO -> enroque_1 ESPECIAL','MOVIMIENTO',2,'p_movimiento','parser.py',56),
  ('MOVIMIENTO -> enroque_2 ESPECIAL','MOVIMIENTO',2,'p_movimiento','parser.py',57),
  ('POS_OPCIONAL -> columna fila','POS_OPCIONAL',2,'p_pos_opcional','parser.py',65),
  ('POS_OPCIONAL -> columna','POS_OPCIONAL',1,'p_pos_opcional','parser.py',66),
  ('POS_OPCIONAL -> fila','POS_OPCIONAL',1,'p_pos_opcional','parser.py',67),
  ('POS -> columna fila','POS',2,'p_pos','parser.py',71),
  ('ESPECIAL -> jaque_mate','ESPECIAL',1,'p_especial','parser.py',75),
  ('ESPECIAL -> jaque','ESPECIAL',1,'p_especial','parser.py',76),
  ('ESPECIAL -> lambda','ESPECIAL',1,'p_especial','parser.py',77),
  ('PIEZA -> pieza','PIEZA',1,'p_pieza','parser.py',81),
  ('PIEZA -> lambda','PIEZA',1,'p_pieza','parser.py',82),
  ('COMENTARIO -> llave_abre COM llave_cierra','COMENTARIO',3,'p_comentario','parser.py',86),
  ('COMENTARIO -> parentecis_abre COM parentecis_cierra','COMENTARIO',3,'p_comentario','parser.py',87),
  ('COMENTARIO -> llave_abre llave_cierra','COMENTARIO',2,'p_comentario','parser.py',88),
  ('COMENTARIO -> parentecis_abre parentecis_cierra','COMENTARIO',2,'p_comentario','parser.py',89),
  ('COM -> COMENTARIO_REAL COM','COM',2,'p_com','parser.py',93),
  ('COM -> MOVIMIENTO_OPCIONAL COM','COM',2,'p_com','parser.py',94),
  ('COM -> COMENTARIO COM','COM',2,'p_com','parser.py',95),
  ('COM -> COMENTARIO_REAL','COM',1,'p_com','parser.py',96),
  ('COM -> MOVIMIENTO_OPCIONAL','COM',1,'p_com','parser.py',97),
  ('COM -> COMENTARIO','COM',1,'p_com','parser.py',98),
  ('COMENTARIO_REAL -> palabra espacio COMENTARIO_REAL','COMENTARIO_REAL',3,'p_comentario_real','parser.py',102),
  ('COMENTARIO_REAL -> palabra','COMENTARIO_REAL',1,'p_comentario_real','parser.py',103),
  ('MOVIMIENTO_OPCIONAL -> NUMERO_OPCIONAL MOVIMIENTO','MOVIMIENTO_OPCIONAL',2,'p_movimiento_opcional','parser.py',107),
  ('NUMERO_OPCIONAL -> NUMERO_JUGADA PUNTOS_OPCIONALES','NUMERO_OPCIONAL',2,'p_numero_opcional','parser.py',111),
  ('PUNTOS_OPCIONALES -> punto','PUNTOS_OPCIONALES',1,'p_puntos_opcionales','parser.py',115),
  ('PUNTOS_OPCIONALES -> punto punto punto','PUNTOS_OPCIONALES',3,'p_puntos_opcionales','parser.py',116),
  ('PUNTOS_OPCIONALES -> lambda','PUNTOS_OPCIONALES',1,'p_puntos_opcionales','parser.py',117),
  ('lambda -> <empty>','lambda',0,'p_lambda','parser.py',121),
]
