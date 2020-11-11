# Copyright (C) 2019-2020  Learnershape and contributors

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np

from .graph_utils import *
from pdb import set_trace
from .helpers import *


def get_objects(cur,q, params=()):
  cur.execute(q, params)
  res = []
  for row in cur.fetchall():
    r = reg(cur, row)
    res.append(r)
  return res


class reg(object):
    def __init__(self, cursor, registro):
         for (attr, val) in zip((d[0] for d in cursor.description),registro) :
            setattr(self, attr, val)
    def __repr__(self):
      if hasattr(self,'id'):
        return 'ID ' + str(self.id)
      else:
        return 'no ID'

class LearnerShapeService:

  def __init__(self,graph, connection):
    self.cur = connection.cursor()
    self.graph = graph

    self.cur =connection.cursor()


  def call(self, ids1, ids2, method):
    """Merge two skills trees into a learnershape,
    taking out focussed skills"""

    if method == 'dag':
      n1,l1 = self.get_ls_skills(ids1)
      n2,l2 = self.get_ls_skills(ids2)

      print(n1)
      print(n2)
      r = merge_trees(n1,l1,n2,l2)

      return {'nodes':r['nodes'], 'links':r['links']}
    elif method == 'graph':
      nodes = []
      edges = []

      USE = {}
      all_ids = ids1 + ids2
      q = "SELECT * FROM embeddings WHERE skill_id=ANY(%s)"
      results = get_objects(self.cur, q, (all_ids, ))
      for r in results:
        USE[r.skill_id] = np.array(r.use)

      for id in ids1:
        name = self.graph.skills[id]['name']
        if id not in USE:
          USE[id] = np.array(0)
        nodes.append({'id': id, 'name': name, 'group':1})

      for id in ids2:
        name = self.graph.skills[id]['name']
        if id not in USE:
          USE[id] = np.array([-0.009504275396466255, -0.03719576448202133, -0.05061517283320427, 0.04743744432926178, 0.003823799081146717, 0.059256624430418015, -0.015820203348994255, 0.03408925607800484, -0.07822452485561371, 0.013407285325229168, -0.053088556975126266, -0.03029940091073513, 0.03160972520709038, 0.0023997128009796143, 0.015125587582588196, -0.025570522993803024, -0.04556047543883324, 0.04775138199329376, 0.08379585295915604, 0.034624237567186356, -0.04304346814751625, -0.07153275609016418, -0.050630033016204834, -0.030498851090669632, 0.005220836494117975, -0.04370444640517235, -0.009454394690692425, -0.07401019334793091, -0.07454603165388107, -0.0494043342769146, -0.06332199275493622, -0.0669034868478775, -0.0680779218673706, 0.002147539285942912, 0.0433429554104805, 0.0194801464676857, 0.05966004356741905, 0.024498838931322098, 0.0017115259543061256, 0.004625261761248112, 0.03894462436437607, 0.05698161944746971, -0.022897783666849136, 0.08478410542011261, -0.04633825272321701, 0.05830768495798111, 0.02441210113465786, 0.0025480587501078844, -0.04831454157829285, -0.019981054589152336, 0.05114232748746872, -0.01595679670572281, 0.08402960002422333, -0.047023672610521317, 0.06365370750427246, 0.02796023339033127, 0.05508476123213768, 0.0033540406730026007, -0.03396008163690567, -0.006633358541876078, 0.009213345125317574, 0.046259235590696335, 0.022548550739884377, -0.07093027234077454, 0.05648501217365265, 0.016268989071249962, 0.04550182819366455, 0.05683691427111626, 0.016307245939970016, 0.005437053740024567, 0.008653685450553894, 0.05432024970650673, -0.00761424982920289, 0.08185950666666031, -0.030019167810678482, -0.049909234046936035, 0.03585420921444893, -0.029614130035042763, -0.011109421029686928, -0.06554418057203293, -0.015606081113219261, 0.03331926465034485, 0.012138948775827885, -0.04464486986398697, -0.00833225343376398, 0.0202893428504467, -0.051642708480358124, 0.008902442641556263, -0.013479385524988174, -0.07536012679338455, 0.04789089411497116, -0.03191419318318367, 0.003836423857137561, -0.0020858573261648417, -0.012879638932645321, -0.03736397251486778, -0.04619153216481209, -0.045942917466163635, 0.0331149660050869, 0.0069787465035915375, -0.02471303939819336, -0.03102235496044159, -0.018876126036047935, -0.012266913428902626, -0.028020577505230904, 0.059544503688812256, 0.06896570324897766, 0.01826757751405239, 0.03573780879378319, -0.016828561201691628, -0.016714924946427345, 0.028862837702035904, 0.02879694290459156, 0.06420307606458664, -0.03525927662849426, 0.05552862584590912, 0.04763856530189514, -0.07370000332593918, -0.06893859803676605, -0.08065646886825562, -0.042194996029138565, 0.010190422646701336, -0.027250254526734352, 0.013394562527537346, 0.07235942780971527, -0.01628832332789898, -0.012524626217782497, -0.01679958961904049, 0.023012738674879074, -0.0001590604952070862, 0.053058922290802, 0.023942604660987854, -0.011064760386943817, 0.011578941717743874, -0.05962634086608887, 0.02234541065990925, 0.02699921652674675, 0.018081093207001686, 0.06820672005414963, -0.06067245453596115, -0.012504823505878448, 0.047393567860126495, -0.0626472532749176, -0.05526651442050934, -0.02760140784084797, -0.05053689703345299, -0.03778192400932312, 0.013094757683575153, -0.004953611176460981, -0.018151070922613144, 0.02409665286540985, -0.0479632243514061, 0.04467250779271126, 0.050970274955034256, -0.04213383421301842, 0.020175769925117493, -0.018233291804790497, -0.08217800408601761, 0.037720538675785065, -0.02414577081799507, -0.061669714748859406, -0.05255482718348503, -0.01837865822017193, -0.004158747382462025, 0.07565736770629883, 0.015321406535804272, -0.0545576810836792, 0.04373186081647873, 0.008890452794730663, 0.0212008785456419, -0.04624137282371521, 0.06366761773824692, -0.04338701441884041, 0.036457404494285583, 0.008628830313682556, -0.027383308857679367, 0.0075056292116642, 0.05461667850613594, -0.05026751384139061, 0.007011771202087402, 0.05565623566508293, -0.002781364368274808, -0.03773590177297592, 0.03044077195227146, -0.008139723911881447, 0.03716861084103584, -0.038655612617731094, -0.062361929565668106, -0.012373753823339939, 0.02065470814704895, 0.028378445655107498, -0.01303898822516203, -0.020936772227287292, -0.048684507608413696, -0.009357394650578499, -0.06960521638393402, 0.05685802921652794, 0.03413016349077225, -0.010777924209833145, 0.008333748206496239, 0.040173035115003586, 0.03577806055545807, -0.010659760795533657, -0.008326878771185875, 0.000894824624992907, -0.03324097767472267, -0.0303608700633049, -0.04881184175610542, 0.04646894708275795, 0.004097689874470234, 0.06256677210330963, -0.009709600359201431, 0.009178470820188522, -0.06409800797700882, -0.004822656512260437, 0.05139481648802757, 0.028294183313846588, 0.045361872762441635, 0.02414051629602909, 0.07168678939342499, 0.07693389803171158, 0.016445817425847054, -0.02879914455115795, 0.06108258664608002, -0.08179817348718643, 0.07325629889965057, 0.05302748084068298, -0.07047317922115326, 0.011343377642333508, 0.011261221021413803, 0.07644031196832657, -0.010889341123402119, 0.010834991000592709, 0.022281793877482414, 0.018038848415017128, 0.014025415293872356, 0.04845881089568138, -0.027873359620571136, -0.057721879333257675, -0.06477786600589752, 0.04064850136637688, -0.003810211783275008, 0.04200664907693863, 0.045148007571697235, 0.04203479737043381, 0.006416501943022013, 0.02795785292983055, -0.020914308726787567, -0.0023483315017074347, 0.0003992915153503418, 0.06384420394897461, 0.03243224695324898, -0.08660560101270676, -0.0113528398796916, 0.00486024422571063, 0.0066154878586530685, 0.053441472351551056, -0.029809333384037018, 0.061145905405282974, -0.01714177057147026, -0.0513906292617321, -0.024956123903393745, -0.04565875977277756, 0.08625724166631699, -0.009282850660383701, -0.03170577436685562, 0.007495644502341747, 0.046376246958971024, 0.05173960700631142, 0.052651043981313705, -0.018198668956756592, -0.044089626520872116, -0.06972305476665497, 0.06338733434677124, -0.06289048492908478, 0.004908578936010599, 0.04975150153040886, -0.052403148263692856, -0.07971682399511337, -0.04905359447002411, 0.056098081171512604, 0.03444666787981987, -0.029436035081744194, 0.05100039765238762, -0.03728939965367317, -0.0374322384595871, -0.020936882123351097, 0.009450409561395645, -0.0070260209031403065, 0.06976845115423203, 0.06188042089343071, -0.06062247231602669, 0.019613727927207947, -0.010079700499773026, -0.009559144265949726, 0.07835312932729721, 0.018727142363786697, 0.0069291661493480206, -0.005934327375143766, 0.026029586791992188, -0.07531660795211792, -0.0067463344894349575, 0.010924572125077248, 0.07125730812549591, 0.06900423020124435, -0.04899412766098976, -0.05506473034620285, 0.021158691495656967, -0.05072825029492378, -0.03917459398508072, 0.03654559329152107, -0.0026887424755841494, -0.058931849896907806, 0.06395922601222992, -0.008978611789643764, -0.023202018812298775, -0.004114218521863222, -0.02463589608669281, -0.05101866275072098, 0.009100706316530704, 0.018125757575035095, -0.057268500328063965, 0.031832803040742874, 0.0549255795776844, -0.0350014753639698, 0.07167605310678482, -0.04804208502173424, -0.02990787848830223, 0.05774897709488869, -0.057591814547777176, -0.054308656603097916, 0.057131752371788025, 0.03810063749551773, -0.03570368140935898, 0.05328407883644104, 0.047224197536706924, 0.02880726382136345, 0.05647232383489609, -0.017490070313215256, -0.07090026885271072, -0.008114572614431381, -0.0023669509682804346, -0.015313937328755856, 0.07147841900587082, -0.007869744673371315, -0.03499922528862953, -0.0050507960841059685, 0.0316871777176857, 0.02643987350165844, -0.051678240299224854, 0.015190115198493004, 0.029605990275740623, -0.0362018421292305, 0.06108236685395241, -0.002787273842841387, 0.06860169023275375, -0.020107373595237732, 0.03294268995523453, -0.033447954803705215, -0.05023029446601868, -0.07849711924791336, -0.03363032639026642, 0.028749175369739532, 0.04024241492152214, 0.02714257873594761, 0.0033010158222168684, 0.0706912949681282, 0.08390401303768158, 0.02297813817858696, 0.07184677571058273, -0.012124059721827507, -0.03670340031385422, 0.08058998733758926, -0.07873726636171341, 0.05497138947248459, -0.046851567924022675, 0.0364062525331974, -0.05003276467323303, 0.05947023630142212, 0.05580415204167366, 0.02036428637802601, 0.07416204363107681, 0.02741030976176262, -0.02299264818429947, -0.020599201321601868, 0.046891193836927414, -0.055530160665512085, 0.07838240265846252, -0.06681744754314423, -0.086203932762146, -0.06593960523605347, -0.022872447967529297, 0.07176925987005234, -0.052380118519067764, 0.08654001355171204, 0.03445912525057793, 0.02259988710284233, 0.044929418712854385, 0.05024145543575287, 0.023572692647576332, 0.03128497302532196, -0.010455185547471046, -0.07049036771059036, -0.01721133105456829, -0.031778790056705475, -0.03421449661254883, -0.04295846447348595, -0.007641591131687164, -0.07347393780946732, 0.06846242398023605, 0.056936852633953094, -0.03936988115310669, 0.01321845781058073, 0.00574121531099081, 0.035213276743888855, 0.054421182721853256, 0.017458181828260422, 0.006466185674071312, 0.08193670958280563, -0.0019476927118375897, 0.005433648359030485, -0.027743039652705193, 0.00008276810694951564, -0.07007265090942383, 0.026668744161725044, -0.02904823236167431, -0.05133429169654846, -0.07525844871997833, 0.022813323885202408, 0.04616706445813179, 0.05205453559756279, 0.06539973616600037, 0.020169809460639954, -0.010874194093048573, -0.023319818079471588, 0.07189645618200302, -0.029109381139278412, -0.042406026273965836, -0.06550323218107224, -0.005217637866735458, 0.01964644528925419, -0.016215015202760696, -0.012796659022569656, 0.020399078726768494, -0.07439146935939789, -0.03433486446738243, -0.02876337058842182, 0.025503581389784813, 0.06260810047388077, 0.00233877613209188, -0.00027234567096456885, -0.0029803430661559105, -0.05414476990699768, 0.01061221957206726, 0.06099996343255043, -0.023165466263890266, 0.07582331448793411, -0.023839375004172325, 0.0151860062032938, -0.06616345793008804, 0.017426947131752968, -0.053922031074762344, 0.03798039257526398, 0.006850524339824915, 0.0568990595638752, 0.05562889948487282, 0.011743836104869843, -0.04911350831389427, -0.03357982635498047, 0.03901003673672676, -0.046840850263834, -0.08161643892526627, 0.08494444191455841, 0.05669553577899933, 0.003705736482515931, 0.06315270066261292, -0.07125992327928543, 0.07418307662010193, 0.07013177126646042, -0.03987137973308563, 0.04773273319005966, -0.032452888786792755, 0.02136252075433731, -0.004714289214462042, -0.06903622299432755, -0.022070446982979774, 0.022962795570492744, 0.0017809109995141625, -0.06747601181268692, 0.01114750001579523, -0.045911964029073715, 0.005112881306558847, -0.06424885243177414, 0.0032843565568327904, 0.03592884913086891, 0.08193530142307281, 0.035559192299842834, -0.04271695762872696, -0.04561791196465492, 0.004215456545352936, 0.07304608821868896, -0.06553062051534653, -0.009355868212878704, -0.022587565705180168, -0.06085328385233879, 0.04349737986922264, 0.05604511871933937, -0.06961566209793091, 0.06986385583877563, -0.044630903750658035, -0.054530397057533264, -0.07576547563076019])
        nodes.append({'id': id, 'name': name, 'group':2})

      dists = []
        
      for src in all_ids:
        for dest in all_ids:
          if src < dest:
            d = np.linalg.norm(USE[src] - USE[dest])
            dists.append(d)

      mean = np.mean(dists)
      std = np.std(dists)

      for src in all_ids:
        for dest in all_ids:
          if src < dest:
            d = np.linalg.norm(USE[src] - USE[dest])
            if d < (mean - std):
              edges.append({'source':src, 'target':dest})
      return({'nodes':nodes, 'links':edges})


  def get_ls_skills(self, skill_ids):
    q = "SELECT * FROM skills WHERE id=ANY(%s)"
    nodes = []
    edges = []
    added_ids = []

    d = get_objects(self.cur,q,(skill_ids,))
    # Assemble one tree into nodes and edges, adding stuff on paths
    for o in d:
      nodes.append({'id':o.id, 'name': o.name})
      added_ids.append(o.id)
      current = o.id
      print(o.id)
      if not o.path_from_root:
        o.path_from_root = [[self.graph.root_id]]
      rev = reversed(o.path_from_root[0])
      for r in rev:
        if r not in added_ids:

            nodes.append({'id':r, 'name': self.graph.skills[r]['name']})
            added_ids.append(r)
        edges.append({'source':r, 'target':current})
        current = r

    return nodes,edges
  

  def get_ls(self,p):
    q = """SELECT * FROM competences INNER JOIN skills ON competences.skill_id = skills.id
WHERE profile_id=%s"""
    nodes = []
    edges = []
    added_ids = []

    d = get_objects(self.cur,q, (p,))
    # Assemble one tree into nodes and edges, adding stuff on paths
    for o in d:
      nodes.append({'id':o.id, 'name': o.name})
      added_ids.append(o.id)
      current = o.id
      print('AUGH ', o)
      rev = reversed(o.path_from_root[0])
      for r in rev:
        if r not in added_ids:
            nodes.append({'id':r, 'name': self.graph.skills[r]['name']})
            added_ids.append(r)
        edges.append({'source':r, 'target':current})
        current = r

    return nodes,edges


  def call_one(self,p1,p2):
    q = """SELECT * FROM competences INNER JOIN skills ON competences.skill_id = skills.id
WHERE profile_id=%s"""
    nodes = []
    edges = []
    added_ids = []

    d = get_objects(self.cur,q,(p1,))

    for o in d:
      nodes.append({'id':o.id, 'name': o.name})
      added_ids.append(o.id)
      current = o.id
      rev = reversed(o.path_from_root[0])
      for r in rev:
        if r not in added_ids:
            nodes.append({'id':r, 'name': self.graph.skills[r]['name']})
            added_ids.append(r)
        edges.append({'source':r, 'target':current})
        current = r

    return{'nodes':nodes, 'links':edges}
      

 

