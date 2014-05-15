if __name__ == "__main__":
    from jarvis import Jarvis
    from database import WordDataBaseBuilder
    from database import TrainingDataBaseBuilder
    from database import AbilitiesDataBaseBuilder
    from database import InnerVoiceDataBaseBuilder
    from interfaces import Console

    wd_builder = WordDataBaseBuilder()
    wd_builder.addTxtFile("learning_material/traning.txt")

    td_builder = TrainingDataBaseBuilder()
    td_builder.addTxtFile("learning_material/traning.txt")

    iv_builder = InnerVoiceDataBaseBuilder()
    iv_builder.addTxtFile("learning_material/inner_voices.txt")

    ab_builder = AbilitiesDataBaseBuilder()

    he = Jarvis()
    he.createWordsDataBase(wd_builder)
    he.createTrainingDataBase(td_builder)
    he.createAbilitiesDataBase(ab_builder)
    he.createInnerVoiceDatabase(iv_builder)
    he.train()

    console = Console()
    console.jarvis(he)
    console.start()

    he.start()

