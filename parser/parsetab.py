
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'comilla corchete_abre corchete_cierra empate enroque_1 enroque_2 espacio gano_blanco gano_negro jaque jaque_mate llave_abre llave_cierra numero_jugada_blanco numero_jugada_negro palabra parentecis_abre parentecis_cierra renglon token_movimientoS    :   METADATA JUGADAS SS    :   METADATA JUGADASS    :   JUGADASS    :   JUGADAS SMETADATA : ITEM_METADATA METADATA\n                | ITEM_METADATAITEM_METADATA  :   corchete_abre palabra espacio comilla COMENTARIO_REAL comilla corchete_cierra renglonJUGADAS  : JUGADA JUGADASJUGADAS  :    MOVIMIENTO_FINAL renglon\n                |    MOVIMIENTO_FINALMOVIMIENTO_FINAL :   gano_blanco\n                        |   gano_negro\n                        |   empateJUGADA   :   numero_jugada_blanco MOVIMIENTO J2JUGADA   :   numero_jugada_blanco MOVIMIENTOJ2   :   COMENTARIO numero_jugada_negro MOVIMIENTO COMENTARIOJ2   :   COMENTARIO numero_jugada_negro MOVIMIENTO J2   :   numero_jugada_negro MOVIMIENTO COMENTARIO J2   :   numero_jugada_negro MOVIMIENTOJ2   :   COMENTARIOJ2   :   MOVIMIENTOJ2   :   MOVIMIENTO COMENTARIOMOVIMIENTO   :   token_movimiento ESPECIALMOVIMIENTO   :   enroque_1 ESPECIAL\n                    |   enroque_1 \n                    |   enroque_2 ESPECIAL\n                    |   enroque_2 MOVIMIENTO   : token_movimientoESPECIAL :   jaque_mate\n                |   jaqueCOMENTARIO   :   llave_abre COM llave_cierraCOMENTARIO  : parentecis_abre parentecis_cierraCOMENTARIO  : parentecis_abre COM parentecis_cierraCOMENTARIO   :    llave_abre llave_cierraCOM  :   palabra\n            |   espacioCOM  :   palabra COM \n            |   espacio COMCOM  :   token_movimiento COM\n            |   token_movimientoCOM  :   COMENTARIO COM\n            |   COMENTARIO COMENTARIO_REAL      :   palabra espacio COMENTARIO_REAL\n                            |   palabra'
    
_lr_action_items = {'corchete_abre':([0,3,4,6,9,10,11,12,15,16,62,],[7,7,7,-10,-11,-12,-13,7,-8,-9,-7,]),'numero_jugada_blanco':([0,2,3,4,5,6,9,10,11,12,14,15,16,18,19,20,21,24,25,26,30,31,32,33,34,36,38,40,45,49,50,51,56,59,62,],[8,8,8,-6,8,-10,-11,-12,-13,8,-5,-8,-9,-15,-28,-25,-27,-21,-14,-20,-23,-29,-30,-24,-26,-22,-19,-34,-32,-17,-18,-31,-33,-16,-7,]),'gano_blanco':([0,2,3,4,5,6,9,10,11,12,14,15,16,18,19,20,21,24,25,26,30,31,32,33,34,36,38,40,45,49,50,51,56,59,62,],[9,9,9,-6,9,-10,-11,-12,-13,9,-5,-8,-9,-15,-28,-25,-27,-21,-14,-20,-23,-29,-30,-24,-26,-22,-19,-34,-32,-17,-18,-31,-33,-16,-7,]),'gano_negro':([0,2,3,4,5,6,9,10,11,12,14,15,16,18,19,20,21,24,25,26,30,31,32,33,34,36,38,40,45,49,50,51,56,59,62,],[10,10,10,-6,10,-10,-11,-12,-13,10,-5,-8,-9,-15,-28,-25,-27,-21,-14,-20,-23,-29,-30,-24,-26,-22,-19,-34,-32,-17,-18,-31,-33,-16,-7,]),'empate':([0,2,3,4,5,6,9,10,11,12,14,15,16,18,19,20,21,24,25,26,30,31,32,33,34,36,38,40,45,49,50,51,56,59,62,],[11,11,11,-6,11,-10,-11,-12,-13,11,-5,-8,-9,-15,-28,-25,-27,-21,-14,-20,-23,-29,-30,-24,-26,-22,-19,-34,-32,-17,-18,-31,-33,-16,-7,]),'$end':([1,3,6,9,10,11,12,13,15,16,22,],[0,-3,-10,-11,-12,-13,-2,-4,-8,-9,-1,]),'renglon':([6,9,10,11,61,],[16,-11,-12,-13,62,]),'palabra':([7,28,29,35,40,41,42,43,44,45,51,56,57,],[17,41,41,47,-34,41,41,41,41,-32,-31,-33,47,]),'token_movimiento':([8,18,19,20,21,27,28,29,30,31,32,33,34,37,40,41,42,43,44,45,51,56,],[19,19,-28,-25,-27,19,43,43,-23,-29,-30,-24,-26,19,-34,43,43,43,43,-32,-31,-33,]),'enroque_1':([8,18,19,20,21,27,30,31,32,33,34,37,],[20,20,-28,-25,-27,20,-23,-29,-30,-24,-26,20,]),'enroque_2':([8,18,19,20,21,27,30,31,32,33,34,37,],[21,21,-28,-25,-27,21,-23,-29,-30,-24,-26,21,]),'espacio':([17,28,29,40,41,42,43,44,45,47,51,56,],[23,42,42,-34,42,42,42,42,-32,57,-31,-33,]),'numero_jugada_negro':([18,19,20,21,26,30,31,32,33,34,40,45,51,56,],[27,-28,-25,-27,37,-23,-29,-30,-24,-26,-34,-32,-31,-33,]),'llave_abre':([18,19,20,21,24,28,29,30,31,32,33,34,38,40,41,42,43,44,45,49,51,56,],[28,-28,-25,-27,28,28,28,-23,-29,-30,-24,-26,28,-34,28,28,28,28,-32,28,-31,-33,]),'parentecis_abre':([18,19,20,21,24,28,29,30,31,32,33,34,38,40,41,42,43,44,45,49,51,56,],[29,-28,-25,-27,29,29,29,-23,-29,-30,-24,-26,29,-34,29,29,29,29,-32,29,-31,-33,]),'jaque_mate':([19,20,21,],[31,31,31,]),'jaque':([19,20,21,],[32,32,32,]),'comilla':([23,47,48,60,],[35,-44,58,-43,]),'llave_cierra':([28,39,40,41,42,43,44,45,51,52,53,54,55,56,],[40,51,-34,-35,-36,-40,-42,-32,-31,-37,-38,-39,-41,-33,]),'parentecis_cierra':([29,40,41,42,43,44,45,46,51,52,53,54,55,56,],[45,-34,-35,-36,-40,-42,-32,56,-31,-37,-38,-39,-41,-33,]),'corchete_cierra':([58,],[61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,3,12,],[1,13,22,]),'METADATA':([0,3,4,12,],[2,2,14,2,]),'JUGADAS':([0,2,3,5,12,],[3,12,3,15,3,]),'ITEM_METADATA':([0,3,4,12,],[4,4,4,4,]),'JUGADA':([0,2,3,5,12,],[5,5,5,5,5,]),'MOVIMIENTO_FINAL':([0,2,3,5,12,],[6,6,6,6,6,]),'MOVIMIENTO':([8,18,27,37,],[18,24,38,49,]),'J2':([18,],[25,]),'COMENTARIO':([18,24,28,29,38,41,42,43,44,49,],[26,36,44,44,50,44,44,44,44,59,]),'ESPECIAL':([19,20,21,],[30,33,34,]),'COM':([28,29,41,42,43,44,],[39,46,52,53,54,55,]),'COMENTARIO_REAL':([35,57,],[48,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> METADATA JUGADAS S','S',3,'p_start','parser.py',16),
  ('S -> METADATA JUGADAS','S',2,'p_start_2','parser.py',32),
  ('S -> JUGADAS','S',1,'p_start_jugadas','parser.py',47),
  ('S -> JUGADAS S','S',2,'p_start_jugadas_s','parser.py',62),
  ('METADATA -> ITEM_METADATA METADATA','METADATA',2,'p_metadata','parser.py',77),
  ('METADATA -> ITEM_METADATA','METADATA',1,'p_metadata','parser.py',78),
  ('ITEM_METADATA -> corchete_abre palabra espacio comilla COMENTARIO_REAL comilla corchete_cierra renglon','ITEM_METADATA',8,'p_item_metadata','parser.py',82),
  ('JUGADAS -> JUGADA JUGADAS','JUGADAS',2,'p_jugadas','parser.py',86),
  ('JUGADAS -> MOVIMIENTO_FINAL renglon','JUGADAS',2,'p_jugadas2','parser.py',92),
  ('JUGADAS -> MOVIMIENTO_FINAL','JUGADAS',1,'p_jugadas2','parser.py',93),
  ('MOVIMIENTO_FINAL -> gano_blanco','MOVIMIENTO_FINAL',1,'p_movimiento_final','parser.py',98),
  ('MOVIMIENTO_FINAL -> gano_negro','MOVIMIENTO_FINAL',1,'p_movimiento_final','parser.py',99),
  ('MOVIMIENTO_FINAL -> empate','MOVIMIENTO_FINAL',1,'p_movimiento_final','parser.py',100),
  ('JUGADA -> numero_jugada_blanco MOVIMIENTO J2','JUGADA',3,'p_jugada','parser.py',109),
  ('JUGADA -> numero_jugada_blanco MOVIMIENTO','JUGADA',2,'p_jugada_2','parser.py',135),
  ('J2 -> COMENTARIO numero_jugada_negro MOVIMIENTO COMENTARIO','J2',4,'p_J2','parser.py',150),
  ('J2 -> COMENTARIO numero_jugada_negro MOVIMIENTO','J2',3,'p_J22','parser.py',158),
  ('J2 -> numero_jugada_negro MOVIMIENTO COMENTARIO','J2',3,'p_J23','parser.py',166),
  ('J2 -> numero_jugada_negro MOVIMIENTO','J2',2,'p_J24','parser.py',174),
  ('J2 -> COMENTARIO','J2',1,'p_J2_comentario','parser.py',182),
  ('J2 -> MOVIMIENTO','J2',1,'p_J2_movimiento','parser.py',188),
  ('J2 -> MOVIMIENTO COMENTARIO','J2',2,'p_J2_movimiento_comentario','parser.py',194),
  ('MOVIMIENTO -> token_movimiento ESPECIAL','MOVIMIENTO',2,'p_movimiento','parser.py',200),
  ('MOVIMIENTO -> enroque_1 ESPECIAL','MOVIMIENTO',2,'p_movimiento_enroque','parser.py',206),
  ('MOVIMIENTO -> enroque_1','MOVIMIENTO',1,'p_movimiento_enroque','parser.py',207),
  ('MOVIMIENTO -> enroque_2 ESPECIAL','MOVIMIENTO',2,'p_movimiento_enroque','parser.py',208),
  ('MOVIMIENTO -> enroque_2','MOVIMIENTO',1,'p_movimiento_enroque','parser.py',209),
  ('MOVIMIENTO -> token_movimiento','MOVIMIENTO',1,'p_movimiento_token_movimiento','parser.py',214),
  ('ESPECIAL -> jaque_mate','ESPECIAL',1,'p_especial','parser.py',219),
  ('ESPECIAL -> jaque','ESPECIAL',1,'p_especial','parser.py',220),
  ('COMENTARIO -> llave_abre COM llave_cierra','COMENTARIO',3,'p_comentario','parser.py',223),
  ('COMENTARIO -> parentecis_abre parentecis_cierra','COMENTARIO',2,'p_comentario_parentesis_abre_solo','parser.py',228),
  ('COMENTARIO -> parentecis_abre COM parentecis_cierra','COMENTARIO',3,'p_comentario_parentesis_abre','parser.py',233),
  ('COMENTARIO -> llave_abre llave_cierra','COMENTARIO',2,'p_comentario_llave_abre_solo','parser.py',238),
  ('COM -> palabra','COM',1,'p_com','parser.py',243),
  ('COM -> espacio','COM',1,'p_com','parser.py',244),
  ('COM -> palabra COM','COM',2,'p_com2','parser.py',250),
  ('COM -> espacio COM','COM',2,'p_com2','parser.py',251),
  ('COM -> token_movimiento COM','COM',2,'p_com3','parser.py',256),
  ('COM -> token_movimiento','COM',1,'p_com3','parser.py',257),
  ('COM -> COMENTARIO COM','COM',2,'p_com4','parser.py',266),
  ('COM -> COMENTARIO','COM',1,'p_com4','parser.py',267),
  ('COMENTARIO_REAL -> palabra espacio COMENTARIO_REAL','COMENTARIO_REAL',3,'p_comentario_real','parser.py',281),
  ('COMENTARIO_REAL -> palabra','COMENTARIO_REAL',1,'p_comentario_real','parser.py',282),
]
