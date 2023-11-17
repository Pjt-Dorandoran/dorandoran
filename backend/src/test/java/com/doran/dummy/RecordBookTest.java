package com.doran.dummy;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.doran.record_book.dto.res.ScriptDto;
import com.doran.record_book.entity.RecordBook;
import com.doran.record_book.mapper.RecordBookMapper;
import com.doran.record_book.repository.RecordBookRepository;

@SpringBootTest
public class RecordBookTest {
    @Autowired
    RecordBookRepository recordBookRepository;

    @Autowired
    RecordBookMapper recordBookMapper;

    @Test
    @DisplayName("대본 넣기")
    // @Transactional
    public void insert() {
        String title = "백설공주";
        AtomicInteger scriptNum = new AtomicInteger(1);
        String[] script = replace();

        Arrays.stream(script)
            .forEach(s -> {
                RecordBook recordBook = recordBookMapper.toRecordBook(title, s, scriptNum.getAndIncrement());

                recordBookRepository.save(recordBook);
            });

        List<ScriptDto> script1 = recordBookRepository.findScript(title);

        for (ScriptDto scriptDto : script1) {
            System.out.println(scriptDto.getScript());
            System.out.println(scriptDto.getScriptNum());
        }
    }

    @DisplayName("정제 진행")
    public String[] replace() {
        String str = "옛날 옛적 한겨울에, 하늘에서 눈송이가 깃털처럼 내리고 있었어요. 그때 어느 왕비가 흑단 나무로 만든 창틀에 앉아 바느질을 하고 있었어요.\n"
            + "눈을 보며 바느질을 하다가 바늘에 손가락이 찔려 피 세 방울을 눈 위로 떨어뜨렸어요.\n"
            + "하얀 눈 속에 있는 피가 너무 아름다워 보여서 왕비는 생각했어요. '눈처럼 하얗고, 피처럼 붉고, 창틀의 나무처럼 까만 머리카락을 가진 아이가 내게 있었다면!'\n"
            + "얼마 지나지 않아 왕비는 딸을 가지게 되었어요. 왕비의 딸은 눈처럼 하얗고, 피처럼 붉었으며 머리카락은 흑단 나무처럼 까매서 '백설공주'라고 불렀어요.\n"
            + "하지만 아이가 태어나자 왕비는 죽고 말았어요. 일 년 후 왕은 새로운 왕비를 아내로 맞이했어요. \n"
            + "자존심이 센 새로운 왕비는 자신보다 더 아름다운 사람이 있는 걸 굉장히 싫어했어요. \n"
            + "새로운 왕비는 신비한 거울을 가지고 있었는데, 그 앞에 서서 거울을 쳐다보며 말했습니다.\n"
            + "\"거울아, 거울아 이 세상에서 누가 가장 아름답니?\" 거울이 대답했습니다. \"왕비님이 이 세상에서 가장 아름다우십니다.\"\n"
            + "왕비는 이 거울이 진실만을 이야기한다는 것을 알았기 때문에 만족했어요. 하지만 백설공주는 자라면서 점점 더 아름다워졌어요. \n"
            + "백설공주가 일곱 살이 되었을 때는 맑은 날처럼 아름다워져 왕비보다 더 예뻐졌어요. \n"
            + "왕비는 거울에게 물었습니다. \"거울아, 거울아 이 세상에서 누가 가장 아름답니?\"\n"
            + "거울이 대답했습니다. \"왕비님이 여기서는 가장 아름다우십니다. 그런데 백설공주가 왕비님보다 천 배 더 아름답습니다.\"\n"
            + "이를 들은 왕비는 깜짝 놀랐고 질투심에 얼굴이 붉으락푸르락했어요. 이후로 왕비는 백설공주를 볼 때마다 심장이 쿵쾅거려 진정되지 않았어요. \n"
            + "그렇게 왕비는 백설공주를 싫어하게 되었습니다. 왕비의 마음속에서 질투심과 높이 자라나, 밤낮으로 진정할 수가 없었어요.\n"
            + "그래서 왕비는 사냥꾼을 불러내 말했습니다. \"더는 백설공주를 내 눈앞에서 보고 싶지 않으니 숲으로 데려가거라. 그리고 그 아이를 죽이고 증거로 폐와 간을 내게 가져오도록 해.\"\n"
            + "사냥꾼은 왕비의 명령에 따라 백설공주를 데리고 숲으로 갔습니다. \n"
            + "그리곤 사냥칼을 꺼내 백설공주의 애꿎은 심장을 찌르려고 하자 백설공주는 울며 말했어요. \"사냥꾼님, 목숨만은 살려주세요! 깊은 숲속으로 가서 다시는 돌아오지 않을게요.\"\n"
            + "백설공주가 너무 아름다웠기 때문에 사냥꾼은 동정심이 생겨 말했어요. \"불쌍한 백설공주야!, 멀리 달아나거라!\"\n"
            + "사냥꾼은 야생동물이 곧 백설공주를 잡아 먹겠다고 생각했어요. 사냥꾼은 백설공주를 죽이지 않아도 되기 때문에 마음속에 박힌 돌을 빼낸 기분이었어요.\n"
            + "그때 어린 멧돼지 한 마리가 사냥꾼에게 껑충 뛰어오고 있었어요. 사냥꾼은 그 어린 멧돼지를 찔러 폐와 간을 꺼내 이를 왕비에게 증거로 가져갔어요. \n"
            + "폐와 간을 본 왕비는 백설공주가 없어졌다고 생각했어요. 가엾은 백설공주는 넓은 숲 속에 완전히 홀로 남겨졌어요.\n"
            + "백설공주는 두려움에 떨며 주위를 둘러보았지만 어떻게 해야할지 몰랐어요. 백설공주는 뾰족한 돌을 넘고, 가시덤불 사이로 달리기 시작했어요.\n"
            + "야생 동물들이 튀어 나오기도 했지만, 백설공주를 해치지는 않았어요. 무서웠던 백설공주는 저녁이 올 때까지 달릴 수 있는 한 오래 달렸어요. 백성공주는 마침내 작은 집 하나를 발견했고, 쉬기 위해 그곳으로 들어갔어요. \n"
            + "백설공주가 들어간 집 안에 있는 모든 물건들은 작았지만, 더없이 사랑스럽고 깨끗했어요. \n"
            + "집에는 흰 식탁보로 덮여 있는 작은 탁자와 접시 일곱 개와 음식이 놓여있었어요. 배고프고 목 말랐던 백설공주는 음식을 조금씩 먹었어요.\n"
            + "백설공주는 너무 피곤해서 침대에 누웠는데, 그 어떤 침대도 백설공주에게 맞지 않았어요. \n"
            + "어떤 침대는 너무 길고 어떤 침대는 너무 짧았는데, 마침 일곱 번째 침대가 딱 맞았어요. 백설공주는 그 위에 누워 편히 잠에 들었습니다.\n"
            + "날이 어두워졌을 때, 광석을 캐러 산에 갔던 집주인 일곱 난쟁이들이 돌아왔어요.\n"
            + "난쟁이들이 초를 켜고 집안이 환해지자 집에 누군가가 앉아있었던 흔적을 발견했어요. \n"
            + "난쟁이들은 이야기 했어요 \"누가 우리집에 왔나봐!!\" 그때 일곱 번째 난쟁이가 침대에 누워 자고 있는 백설공주를 발견하였습니다.\n"
            + "일곱 번째 난쟁이는 다른 난쟁이들을 불렀고, 촛불을 들고 와 백설공주를 비췄습니다.\n"
            + "\"오, 세상에나, 오, 세상에!\" 난쟁이들이 소리쳤습니다. 이 아름다운 소녀는 누구지?\" 난쟁이들은 너무 기뻐서 백설공주를 깨우지 않고 자도록 내버려 두었습니다.\n"
            + "아침이 되자 백설공주가 깨어났고, 일곱 난쟁이를 보고 깜짝 놀랐습니다. 그러나 난쟁이들은 백설공주에게 상냥하게 대하며 많은 이야기를 나누었어요. \n"
            + "백설공주는 자신의 계모가 자신을 죽이려고 했던 일, 사냥꾼이 자신을 살려주었던 일을 난쟁이에게 이야기해주었습니다.\n"
            + "난쟁이들은 불쌍한 백설공주를 자기들 집에서 지낼 수 있게 허락했어요. 그리고는 백설공주에게 주의를 주었습니다. \n"
            + "\"계모를 조심해! 계모는 네가 여기에 있다는 것을 곧 알게 될 거야. 아무도 집으로 들이면 안돼!\"\n"
            + "한편 백설공주가 없어졌다고 생각한 왕비는 자신이 가장 예쁜 사람이라고 생각했어요. \"거울아, 거울아, 이 세상에서 누가 가장 아름답니?\"\n"
            + "거울이 대답했어요. \"왕비님이 여기서 가장 아름다우십니다. 하지만 산 속에서 일곱 난쟁이와 함께 살고 있는 백설공주가 왕비님보다 여전히 천 배 더 아름답습니다.\"\n"
            + "거울은 거짓말을 하지 않는다는 것을 알았기 때문에 왕비는 놀랐어요.  사냥꾼이 자신을 속였고 백설공주가 여전히 살아있다는 사실을 깨달았어요. \n"
            + "왕비는 백설공주를 어떻게 죽일지 생각하고 또 생각했어요. 거울의 말을 듣자 왕비는 분노에 치를 떨었어요. \n"
            + "왕비가 소리 쳤습니다. \"내 인생을 바쳐서라도 백설공주를 죽이고 말 테야!\"  이 후, 아무도 들어가지 않는 비밀스럽고 외딴 방에 들어가 빨간 독사과를 만들었어요. \n"
            + "왕비는 분장을 하고 늙은 농부처럼 옷을 입었어요. 그리고 산봉우리 일곱 개를 넘어 난쟁이의 집으로 가 문을 두드렸어요.\n"
            + "\"아가씨 이 맛있는 사과 좀 먹어봐요\" 늙은 농부가 말했어요. 백설공주는 예쁘고 빨간 사과를 보곤 잡곤 한 입 베어 먹었어요.\n"
            + "\"어어.. 갑자기 너무 어지러워요\" 백설공주가 희미하게 말했어요. 독이 든 사과를 먹은 백설 공주는 쓰러져 죽게 되었어요.\n"
            + "늙은 농부는 섬뜩한 눈빛으로 크게 웃었어요. \"백설공주! 드디어 너가 죽었구나!\" 그리고 집으로 돌아와서 거울에게 물었습니다.\n"
            + "\"거울아, 벽에 있는 거울아, 이 세상에서 누가 가장 아름답니?\" 그러자 거울이 마침내 대답했습니다. \"왕비님이 여기서 가장 아름다우십니다.\n"
            + "왕비는 드디어 흡족한 표정을 짓게 되었어요. 집으로 돌아온 난쟁이들은 바닥에 쓰러져 있는 백설공주를 발견했어요.\n"
            + "\"백설공주!! 백설공주!! 일어나!!\" 난쟁이들은 펑펑 울기 시작했어요. 난쟁이들은 슬퍼하며 유리로 만든 관에 백설공주를 눕혔어요.\n"
            + "그 때, 이웃나라 왕자가 그 곳을 지나고 있었어요. \"아니 이렇게 예쁜 공주가 있었다니!\"\n"
            + "왕자가 조심스럽게 백설공주를 일으키자 백설공주의 입에서 사과 조각이 튀어나왔어요.\n"
            + "기침을 하며 눈을 뜬 백설공주는 왕자를 보며 말했어요. \"당신이 저를 살려주셨군요!\"\n"
            + "일곱 난쟁이와 왕자는 신나서 어쩔 줄 몰라했어요. \n"
            + "\"아름다운 공주님! 저와 결혼해 주시겠어요?\" 왕자가 말했어요. 이를 허락한 백설공주는 난쟁이들의 축복 속에 결혼식을 올리게 되었어요.\n"
            + "어느 날 왕비는 거울에게 물었어요. \"거울아, 거울아, 이 세상에서 누가 가장 아름답니?\"\n"
            + "\"이웃나라 왕자와 결혼한 왕비가 천 배 더 아름답습니다.\" 왕비는 너무도 화가 난 나머지 소리를 지르다가 그만 추하고 늙은 마녀의 모습으로 변하고 말았어요.\n"
            + "그리고 다시는 원래 모습으로 돌아가지 못했답니다.";

        return str.split("\\n+");
    }
}