import pvfalcon

class AudioProcessor:

    def __init__(self, access_key=None):
        self._key = "cOwG35mEtFF/HzAxdHQVV3Ft4mLpDOmuELpVNwsdDGBQE0keC0bRGQ==" or access_key
        self._falcon = pvfalcon.create(access_key=self._key)

    def processAudio(self, file_path):
        """
        Segments the audiofile based on who is speaking.
        :param file_path: filepath to the audiofile
        :return: list of segments that has timestamps of who spoke when
        """
        segments = self._falcon.process_file(file_path)
        for segment in segments:
            print(
                "{speaker_tag=%d start_sec=%.2f end_sec=%.2f}"
                % (segment.speaker_tag, segment.start_sec, segment.end_sec)
            )

        self._falcon.delete()
        return segments



