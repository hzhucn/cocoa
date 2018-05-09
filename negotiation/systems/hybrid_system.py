from cocoa.systems.rulebased_system import RulebasedSystem as BaseRulebasedSystem
from sessions.hybrid_session import HybridSession

def add_hybrid_system_arguments(parser):
    parser.add_argument('--templates', help='Path to templates (.pkl)')
    parser.add_argument('--checkpoint', default='.', help='Directory to save learned models')

class HybridSystem(BaseRulebasedSystem):

    def _new_session(self, agent, kb, config=None):
        manager_session = self.manager.new_session(agent, kb)
        return HybridSession.get_session(agent, kb, self.lexicon,
                self.generator, manager_session)

    @classmethod
    def name(cls):
        return 'hybrid'

