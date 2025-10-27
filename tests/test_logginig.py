from mgimo.utils.logging import Mark, Transcript


def test_user_with_two_marks(tmp_path):
    path = tmp_path / "some.json"
    m = Mark("Упражнение 1").score(points=3, out_of=5)
    m.save(path)
    t = Transcript()
    t.register(path)
    t.register(path)
    assert t.summary.percent == 60 and t.summary.out_of == 10
