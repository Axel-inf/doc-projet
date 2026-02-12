class DocumentInfos:

    title = u"Développement d'une application mobile de planification des devoirs et des examens"
    first_name = 'Axel'
    last_name = 'Reichenbach'
    second_first_name = 'Arno'  # À adapter
    second_last_name = 'Varin'       # À adapter
    author = f'{first_name} {last_name} et {second_first_name} {second_last_name}'
    year = u'2026'
    month = u'Février'
    seminary_title = u'Projet OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/Axel-inf/doc-projet"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()