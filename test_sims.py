import unittest
import os

try:
    import mujoco_py
    from mujoco_py import load_model_from_path, MjSim, MjViewer, load_model_from_xml, ignore_mujoco_warnings
except ImportError as e:
    raise ImportError("(HINT: you need to install mujoco_py, and also perform the setup instructions here: https://github.com/openai/mujoco-py/.)")


model_paths = [
            # Basic models
            "basic/myomuscle.xml",

            # finger models
            "finger/finger_v0.xml",
            "finger/myofinger_v0.xml",
            "finger/motorfinger_v0.xml",

            # elbow models
            "elbow/myoelbow_1dof6muscles_1dofexo.xml",
            "elbow/myoelbow_1dof6muscles.xml",
            "elbow/myoelbow_2dof6muscles.xml",
            "elbow/myoelbow_1dof6muscles_1dofSoftexo_Ideal.xml",
            "elbow/myoelbow_1dof6muscles_1dofSoftexo_sim2.xml",

            # hand models
            "hand/myohand.xml",

            # gait models
            "leg/myolegs_v0.52(mj210).mjb",
            # "leg/myolegs_v0.52(mj234).mjb", # test with mj234 leg/myoleg_v0.52\(mj234\).mjb
        ]

class TestSims(unittest.TestCase):

    def get_sim(self, model_path:str=None, model_xmlstr=None):
        """
        Get sim using model_path or model_xmlstr.
        """
        if model_path:
            if model_path.startswith("/"):
                fullpath = model_path
            else:
                fullpath = os.path.join(os.path.dirname(__file__), model_path)
            if not os.path.exists(fullpath):
                raise IOError("File %s does not exist" % fullpath)
            model = load_model_from_path(fullpath)
        elif model_xmlstr:
            model = load_model_from_xml(model_xmlstr)
        else:
            raise TypeError("Both model_path and model_xmlstr can't be None")

        return MjSim(model)


    def test_sims(self):

        for model_path in model_paths:
            print("Testing: {}".format(model_path))
            self.get_sim(model_path)


if __name__ == '__main__':
    unittest.main()

