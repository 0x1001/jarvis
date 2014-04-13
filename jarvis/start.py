if __name__ == "__main__":
    from jarvis import Jarvis
    from database import WordDataBaseBuilder
    from database import TrainingDataBaseBuilder
    from database import AbilitiesDataBaseBuilder

    wd_builder = WordDataBaseBuilder()
    wd_builder.addTxtFile("learning_material/traning.txt")

    td_builder = TrainingDataBaseBuilder()
    td_builder.addTxtFile("learning_material/traning.txt")

    ab_builder = AbilitiesDataBaseBuilder()

    he = Jarvis()
    he.createWordsDataBase(wd_builder)
    he.createTrainingDataBase(td_builder)
    he.createAbilitiesDataBase(ab_builder)
    he.train()

    print he.respond("how are you")
    print he.respond("what time is it")