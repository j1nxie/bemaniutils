import random
import time
from typing import Any, Dict, Optional, Tuple

from bemani.client.base import BaseClient
from bemani.protocol import Node


class IIDXCopulaClient(BaseClient):
    NAME = "TEST"

    def verify_iidx23shop_getname(self, lid: str) -> str:
        call = self.call_node()

        # Construct node
        IIDX23shop = Node.void("IIDX23shop")
        call.add_child(IIDX23shop)
        IIDX23shop.set_attribute("method", "getname")
        IIDX23shop.set_attribute("lid", lid)

        # Swap with server
        resp = self.exchange("", call)

        # Verify that response is correct
        self.assert_path(resp, "response/IIDX23shop/@opname")
        self.assert_path(resp, "response/IIDX23shop/@pid")
        self.assert_path(resp, "response/IIDX23shop/@cls_opt")

        return resp.child("IIDX23shop").attribute("opname")

    def verify_iidx23shop_savename(self, lid: str, name: str) -> None:
        call = self.call_node()

        # Construct node
        IIDX23shop = Node.void("IIDX23shop")
        IIDX23shop.set_attribute("lid", lid)
        IIDX23shop.set_attribute("pid", "51")
        IIDX23shop.set_attribute("method", "savename")
        IIDX23shop.set_attribute("cls_opt", "0")
        IIDX23shop.set_attribute("ccode", "US")
        IIDX23shop.set_attribute("opname", name)
        IIDX23shop.set_attribute("rcode", ".")

        call.add_child(IIDX23shop)

        # Swap with server
        resp = self.exchange("", call)

        # Verify that response is correct
        self.assert_path(resp, "response/IIDX23shop")

    def verify_iidx23pc_common(self) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("method", "common")

        # Swap with server
        resp = self.exchange("", call)

        # Verify that response is correct
        self.assert_path(resp, "response/IIDX23pc/ir/@beat")
        self.assert_path(resp, "response/IIDX23pc/newsong_another/@open")
        self.assert_path(resp, "response/IIDX23pc/boss/@phase")
        self.assert_path(resp, "response/IIDX23pc/event1_phase/@phase")
        self.assert_path(resp, "response/IIDX23pc/event2_phase/@phase")
        self.assert_path(resp, "response/IIDX23pc/extra_boss_event/@phase")
        self.assert_path(resp, "response/IIDX23pc/bemani_summer2016/@phase")
        self.assert_path(resp, "response/IIDX23pc/expert/@phase")
        self.assert_path(resp, "response/IIDX23pc/expert_random_select/@phase")

    def verify_iidx23music_crate(self) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23music")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("method", "crate")

        # Swap with server
        resp = self.exchange("", call)

        self.assert_path(resp, "response/IIDX23music")
        for child in resp.child("IIDX23music").children:
            if child.name != "c":
                raise Exception(f"Invalid node {child} in clear rate response!")
            if len(child.value) != 12:
                raise Exception(f"Invalid node data {child} in clear rate response!")
            for v in child.value:
                if v < 0 or v > 101:
                    raise Exception(f"Invalid clear percent {child} in clear rate response!")

    def verify_iidx23shop_getconvention(self, lid: str) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23shop")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("method", "getconvention")
        IIDX23pc.set_attribute("lid", lid)

        # Swap with server
        resp = self.exchange("", call)

        # Verify that response is correct
        self.assert_path(resp, "response/IIDX23shop/valid")
        self.assert_path(resp, "response/IIDX23shop/@music_0")
        self.assert_path(resp, "response/IIDX23shop/@music_1")
        self.assert_path(resp, "response/IIDX23shop/@music_2")
        self.assert_path(resp, "response/IIDX23shop/@music_3")

    def verify_iidx23pc_visit(self, extid: int, lid: str) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("iidxid", str(extid))
        IIDX23pc.set_attribute("lid", lid)
        IIDX23pc.set_attribute("method", "visit")
        IIDX23pc.set_attribute("pid", "51")

        # Swap with server
        resp = self.exchange("", call)

        # Verify that response is correct
        self.assert_path(resp, "response/IIDX23pc/@aflg")
        self.assert_path(resp, "response/IIDX23pc/@anum")
        self.assert_path(resp, "response/IIDX23pc/@pflg")
        self.assert_path(resp, "response/IIDX23pc/@pnum")
        self.assert_path(resp, "response/IIDX23pc/@sflg")
        self.assert_path(resp, "response/IIDX23pc/@snum")

    def verify_iidx23ranking_getranker(self, lid: str) -> None:
        for clid in [0, 1, 2, 3, 4, 5, 6]:
            call = self.call_node()

            # Construct node
            IIDX23pc = Node.void("IIDX23ranking")
            call.add_child(IIDX23pc)
            IIDX23pc.set_attribute("method", "getranker")
            IIDX23pc.set_attribute("lid", lid)
            IIDX23pc.set_attribute("clid", str(clid))

            # Swap with server
            resp = self.exchange("", call)

            # Verify that response is correct
            self.assert_path(resp, "response/IIDX23ranking")

    def verify_iidx23shop_sentinfo(self, lid: str) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23shop")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("method", "sentinfo")
        IIDX23pc.set_attribute("lid", lid)
        IIDX23pc.set_attribute("bflg", "1")
        IIDX23pc.set_attribute("bnum", "2")
        IIDX23pc.set_attribute("ioid", "0")
        IIDX23pc.set_attribute("tax_phase", "0")

        # Swap with server
        resp = self.exchange("", call)

        # Verify that response is correct
        self.assert_path(resp, "response/IIDX23shop")

    def verify_iidx23pc_get(self, ref_id: str, card_id: str, lid: str) -> Dict[str, Any]:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("rid", ref_id)
        IIDX23pc.set_attribute("did", ref_id)
        IIDX23pc.set_attribute("pid", "51")
        IIDX23pc.set_attribute("lid", lid)
        IIDX23pc.set_attribute("cid", card_id)
        IIDX23pc.set_attribute("method", "get")
        IIDX23pc.set_attribute("ctype", "1")

        # Swap with server
        resp = self.exchange("", call)

        # Verify that the response is correct
        self.assert_path(resp, "response/IIDX23pc/pcdata/@name")
        self.assert_path(resp, "response/IIDX23pc/pcdata/@pid")
        self.assert_path(resp, "response/IIDX23pc/pcdata/@id")
        self.assert_path(resp, "response/IIDX23pc/pcdata/@idstr")
        self.assert_path(resp, "response/IIDX23pc/deller")
        self.assert_path(resp, "response/IIDX23pc/secret/flg1")
        self.assert_path(resp, "response/IIDX23pc/secret/flg2")
        self.assert_path(resp, "response/IIDX23pc/secret/flg3")
        self.assert_path(resp, "response/IIDX23pc/achievements/trophy")
        self.assert_path(resp, "response/IIDX23pc/skin")
        self.assert_path(resp, "response/IIDX23pc/grade")
        self.assert_path(resp, "response/IIDX23pc/ir_data")
        self.assert_path(resp, "response/IIDX23pc/secret_course_data")
        self.assert_path(resp, "response/IIDX23pc/rlist")
        self.assert_path(resp, "response/IIDX23pc/step")
        self.assert_path(resp, "response/IIDX23pc/favorite/sp_mlist")
        self.assert_path(resp, "response/IIDX23pc/favorite/sp_clist")
        self.assert_path(resp, "response/IIDX23pc/favorite/dp_mlist")
        self.assert_path(resp, "response/IIDX23pc/favorite/dp_clist")

        name = resp.child("IIDX23pc/pcdata").attribute("name")
        if name != self.NAME:
            raise Exception(f"Invalid name '{name}' returned for Ref ID '{ref_id}'")

        # Extract and return account data
        ir_data: Dict[int, Dict[int, Dict[str, int]]] = {}
        for child in resp.child("IIDX23pc/ir_data").children:
            if child.name == "e":
                course_id = child.value[0]
                course_chart = child.value[1]
                clear_status = child.value[2]
                pgnum = child.value[3]
                gnum = child.value[4]

                if course_id not in ir_data:
                    ir_data[course_id] = {}
                ir_data[course_id][course_chart] = {
                    "clear_status": clear_status,
                    "pgnum": pgnum,
                    "gnum": gnum,
                }

        secret_course_data: Dict[int, Dict[int, Dict[str, int]]] = {}
        for child in resp.child("IIDX23pc/secret_course_data").children:
            if child.name == "e":
                course_id = child.value[0]
                course_chart = child.value[1]
                clear_status = child.value[2]
                pgnum = child.value[3]
                gnum = child.value[4]

                if course_id not in secret_course_data:
                    secret_course_data[course_id] = {}
                secret_course_data[course_id][course_chart] = {
                    "clear_status": clear_status,
                    "pgnum": pgnum,
                    "gnum": gnum,
                }

        expert_point: Dict[int, Dict[str, int]] = {}
        for child in resp.child("IIDX23pc/expert_point").children:
            if child.name == "detail":
                expert_point[int(child.attribute("course_id"))] = {
                    "n_point": int(child.attribute("n_point")),
                    "h_point": int(child.attribute("h_point")),
                    "a_point": int(child.attribute("a_point")),
                }

        return {
            "extid": int(resp.child("IIDX23pc/pcdata").attribute("id")),
            "sp_dan": int(resp.child("IIDX23pc/grade").attribute("sgid")),
            "dp_dan": int(resp.child("IIDX23pc/grade").attribute("dgid")),
            "deller": int(resp.child("IIDX23pc/deller").attribute("deller")),
            "ir_data": ir_data,
            "secret_course_data": secret_course_data,
            "expert_point": expert_point,
        }

    def verify_iidx23music_getrank(self, extid: int) -> Dict[int, Dict[int, Dict[str, int]]]:
        scores: Dict[int, Dict[int, Dict[str, int]]] = {}
        for cltype in [0, 1]:  # singles, doubles
            call = self.call_node()

            # Construct node
            IIDX23music = Node.void("IIDX23music")
            call.add_child(IIDX23music)
            IIDX23music.set_attribute("method", "getrank")
            IIDX23music.set_attribute("iidxid", str(extid))
            IIDX23music.set_attribute("cltype", str(cltype))

            # Swap with server
            resp = self.exchange("", call)

            self.assert_path(resp, "response/IIDX23music/style")
            if int(resp.child("IIDX23music/style").attribute("type")) != cltype:
                raise Exception("Returned wrong clear type for IIDX23music.getrank!")

            for child in resp.child("IIDX23music").children:
                if child.name == "m":
                    if child.value[0] != -1:
                        raise Exception("Got non-self score back when requesting only our scores!")

                    music_id = child.value[1]
                    normal_clear_status = child.value[2]
                    hyper_clear_status = child.value[3]
                    another_clear_status = child.value[4]
                    normal_ex_score = child.value[5]
                    hyper_ex_score = child.value[6]
                    another_ex_score = child.value[7]
                    normal_miss_count = child.value[8]
                    hyper_miss_count = child.value[9]
                    another_miss_count = child.value[10]

                    if cltype == 0:
                        normal = 0
                        hyper = 1
                        another = 2
                    else:
                        normal = 3
                        hyper = 4
                        another = 5

                    if music_id not in scores:
                        scores[music_id] = {}

                    scores[music_id][normal] = {
                        "clear_status": normal_clear_status,
                        "ex_score": normal_ex_score,
                        "miss_count": normal_miss_count,
                    }
                    scores[music_id][hyper] = {
                        "clear_status": hyper_clear_status,
                        "ex_score": hyper_ex_score,
                        "miss_count": hyper_miss_count,
                    }
                    scores[music_id][another] = {
                        "clear_status": another_clear_status,
                        "ex_score": another_ex_score,
                        "miss_count": another_miss_count,
                    }
                elif child.name == "b":
                    music_id = child.value[0]
                    clear_status = child.value[1]

                    scores[music_id][6] = {
                        "clear_status": clear_status,
                        "ex_score": -1,
                        "miss_count": -1,
                    }

        return scores

    def verify_iidx23pc_save(
        self,
        extid: int,
        card: str,
        lid: str,
        expert_point: Optional[Dict[str, int]] = None,
    ) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("s_disp_judge", "1")
        IIDX23pc.set_attribute("mode", "6")
        IIDX23pc.set_attribute("pmode", "0")
        IIDX23pc.set_attribute("method", "save")
        IIDX23pc.set_attribute("s_sorttype", "0")
        IIDX23pc.set_attribute("s_exscore", "0")
        IIDX23pc.set_attribute("d_notes", "0.000000")
        IIDX23pc.set_attribute("gpos", "0")
        IIDX23pc.set_attribute("s_gno", "8")
        IIDX23pc.set_attribute("s_hispeed", "5.771802")
        IIDX23pc.set_attribute("s_judge", "0")
        IIDX23pc.set_attribute("d_timing", "0")
        IIDX23pc.set_attribute("rtype", "0")
        IIDX23pc.set_attribute("d_largejudge", "0")
        IIDX23pc.set_attribute("d_lift", "60")
        IIDX23pc.set_attribute("s_pace", "0")
        IIDX23pc.set_attribute("d_exscore", "0")
        IIDX23pc.set_attribute("d_sdtype", "0")
        IIDX23pc.set_attribute("s_opstyle", "1")
        IIDX23pc.set_attribute("s_achi", "449")
        IIDX23pc.set_attribute("s_largejudge", "0")
        IIDX23pc.set_attribute("d_gno", "0")
        IIDX23pc.set_attribute("s_lift", "60")
        IIDX23pc.set_attribute("s_notes", "31.484070")
        IIDX23pc.set_attribute("d_tune", "0")
        IIDX23pc.set_attribute("d_sdlen", "0")
        IIDX23pc.set_attribute("d_achi", "4")
        IIDX23pc.set_attribute("d_opstyle", "0")
        IIDX23pc.set_attribute("sp_opt", "8208")
        IIDX23pc.set_attribute("iidxid", str(extid))
        IIDX23pc.set_attribute("lid", lid)
        IIDX23pc.set_attribute("s_judgeAdj", "0")
        IIDX23pc.set_attribute("s_tune", "3")
        IIDX23pc.set_attribute("s_sdtype", "1")
        IIDX23pc.set_attribute("s_gtype", "2")
        IIDX23pc.set_attribute("d_judge", "0")
        IIDX23pc.set_attribute("cid", card)
        IIDX23pc.set_attribute("cltype", "0")
        IIDX23pc.set_attribute("ctype", "1")
        IIDX23pc.set_attribute("bookkeep", "0")
        IIDX23pc.set_attribute("d_hispeed", "0.000000")
        IIDX23pc.set_attribute("d_pace", "0")
        IIDX23pc.set_attribute("d_judgeAdj", "0")
        IIDX23pc.set_attribute("s_timing", "1")
        IIDX23pc.set_attribute("d_disp_judge", "0")
        IIDX23pc.set_attribute("s_sdlen", "121")
        IIDX23pc.set_attribute("dp_opt2", "0")
        IIDX23pc.set_attribute("d_gtype", "0")
        IIDX23pc.set_attribute("d_sorttype", "0")
        IIDX23pc.set_attribute("dp_opt", "0")
        pyramid = Node.void("pyramid")
        IIDX23pc.add_child(pyramid)
        pyramid.set_attribute("point", "290")
        destiny_catharsis = Node.void("destiny_catharsis")
        IIDX23pc.add_child(destiny_catharsis)
        destiny_catharsis.set_attribute("point", "290")
        bemani_summer_collabo = Node.void("bemani_summer_collabo")
        IIDX23pc.add_child(bemani_summer_collabo)
        bemani_summer_collabo.set_attribute("point", "290")
        deller = Node.void("deller")
        IIDX23pc.add_child(deller)
        deller.set_attribute("deller", "150")

        if expert_point is not None:
            epnode = Node.void("expert_point")
            epnode.set_attribute("h_point", str(expert_point["h_point"]))
            epnode.set_attribute("course_id", str(expert_point["course_id"]))
            epnode.set_attribute("n_point", str(expert_point["n_point"]))
            epnode.set_attribute("a_point", str(expert_point["a_point"]))
            IIDX23pc.add_child(epnode)

        # Swap with server
        resp = self.exchange("", call)
        self.assert_path(resp, "response/IIDX23pc")

    def verify_iidx23music_reg(self, extid: int, lid: str, score: Dict[str, Any]) -> None:
        call = self.call_node()

        # Construct node
        IIDX23music = Node.void("IIDX23music")
        call.add_child(IIDX23music)
        IIDX23music.set_attribute("convid", "-1")
        IIDX23music.set_attribute("iidxid", str(extid))
        IIDX23music.set_attribute("pgnum", str(score["pgnum"]))
        IIDX23music.set_attribute("pid", "51")
        IIDX23music.set_attribute("rankside", "1")
        IIDX23music.set_attribute("cflg", str(score["clear_status"]))
        IIDX23music.set_attribute("method", "reg")
        IIDX23music.set_attribute("gnum", str(score["gnum"]))
        IIDX23music.set_attribute("clid", str(score["chart"]))
        IIDX23music.set_attribute("mnum", str(score["mnum"]))
        IIDX23music.set_attribute("is_death", "0")
        IIDX23music.set_attribute("theory", "0")
        IIDX23music.set_attribute("shopconvid", lid)
        IIDX23music.set_attribute("mid", str(score["id"]))
        IIDX23music.set_attribute("shopflg", "1")
        IIDX23music.add_child(Node.binary("ghost", bytes([1] * 64)))

        # Swap with server
        resp = self.exchange("", call)
        self.assert_path(resp, "response/IIDX23music/shopdata/@rank")
        self.assert_path(resp, "response/IIDX23music/ranklist/data")

    def verify_iidx23music_appoint(self, extid: int, musicid: int, chart: int) -> Tuple[int, bytes]:
        call = self.call_node()

        # Construct node
        IIDX23music = Node.void("IIDX23music")
        call.add_child(IIDX23music)
        IIDX23music.set_attribute("clid", str(chart))
        IIDX23music.set_attribute("method", "appoint")
        IIDX23music.set_attribute("ctype", "0")
        IIDX23music.set_attribute("iidxid", str(extid))
        IIDX23music.set_attribute("subtype", "")
        IIDX23music.set_attribute("mid", str(musicid))

        # Swap with server
        resp = self.exchange("", call)
        self.assert_path(resp, "response/IIDX23music/mydata/@score")

        return (
            int(resp.child("IIDX23music/mydata").attribute("score")),
            resp.child_value("IIDX23music/mydata"),
        )

    def verify_iidx23pc_reg(self, ref_id: str, card_id: str, lid: str) -> int:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        call.add_child(IIDX23pc)
        IIDX23pc.set_attribute("lid", lid)
        IIDX23pc.set_attribute("pid", "51")
        IIDX23pc.set_attribute("method", "reg")
        IIDX23pc.set_attribute("cid", card_id)
        IIDX23pc.set_attribute("did", ref_id)
        IIDX23pc.set_attribute("rid", ref_id)
        IIDX23pc.set_attribute("name", self.NAME)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23pc/@id")
        self.assert_path(resp, "response/IIDX23pc/@id_str")

        return int(resp.child("IIDX23pc").attribute("id"))

    def verify_iidx23pc_playstart(self) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        IIDX23pc.set_attribute("method", "playstart")
        IIDX23pc.set_attribute("side", "1")
        call.add_child(IIDX23pc)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23pc")

    def verify_iidx23music_play(self, score: Dict[str, int]) -> None:
        call = self.call_node()

        # Construct node
        IIDX23music = Node.void("IIDX23music")
        IIDX23music.set_attribute("opt", "64")
        IIDX23music.set_attribute("clid", str(score["chart"]))
        IIDX23music.set_attribute("mid", str(score["id"]))
        IIDX23music.set_attribute("gnum", str(score["gnum"]))
        IIDX23music.set_attribute("cflg", str(score["clear_status"]))
        IIDX23music.set_attribute("pgnum", str(score["pgnum"]))
        IIDX23music.set_attribute("pid", "51")
        IIDX23music.set_attribute("method", "play")
        call.add_child(IIDX23music)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23music/@clid")
        self.assert_path(resp, "response/IIDX23music/@crate")
        self.assert_path(resp, "response/IIDX23music/@frate")
        self.assert_path(resp, "response/IIDX23music/@mid")

    def verify_iidx23pc_playend(self) -> None:
        call = self.call_node()

        # Construct node
        IIDX23pc = Node.void("IIDX23pc")
        IIDX23pc.set_attribute("cltype", "0")
        IIDX23pc.set_attribute("bookkeep", "0")
        IIDX23pc.set_attribute("mode", "1")
        IIDX23pc.set_attribute("method", "playend")
        call.add_child(IIDX23pc)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23pc")

    def verify_iidx23music_breg(self, iidxid: int, score: Dict[str, int]) -> None:
        call = self.call_node()

        # Construct node
        IIDX23music = Node.void("IIDX23music")
        IIDX23music.set_attribute("gnum", str(score["gnum"]))
        IIDX23music.set_attribute("iidxid", str(iidxid))
        IIDX23music.set_attribute("mid", str(score["id"]))
        IIDX23music.set_attribute("method", "breg")
        IIDX23music.set_attribute("pgnum", str(score["pgnum"]))
        IIDX23music.set_attribute("cflg", str(score["clear_status"]))
        call.add_child(IIDX23music)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23music")

    def verify_iidx23grade_raised(self, iidxid: int, shop_name: str, dantype: str) -> None:
        call = self.call_node()

        # Construct node
        IIDX23grade = Node.void("IIDX23grade")
        IIDX23grade.set_attribute("opname", shop_name)
        IIDX23grade.set_attribute("is_mirror", "0")
        IIDX23grade.set_attribute("oppid", "51")
        IIDX23grade.set_attribute("achi", "50")
        IIDX23grade.set_attribute("cstage", "4")
        IIDX23grade.set_attribute("gid", "5")
        IIDX23grade.set_attribute("iidxid", str(iidxid))
        IIDX23grade.set_attribute("gtype", "0" if dantype == "sp" else "1")
        IIDX23grade.set_attribute("is_ex", "0")
        IIDX23grade.set_attribute("pside", "0")
        IIDX23grade.set_attribute("method", "raised")
        call.add_child(IIDX23grade)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23grade/@pnum")

    def verify_iidx23ranking_entry(self, iidxid: int, shop_name: str, coursetype: str) -> None:
        call = self.call_node()

        # Construct node
        IIDX23ranking = Node.void("IIDX23ranking")
        IIDX23ranking.set_attribute("opname", shop_name)
        IIDX23ranking.set_attribute("clr", "4")
        IIDX23ranking.set_attribute("pgnum", "1771")
        IIDX23ranking.set_attribute("coid", "2")
        IIDX23ranking.set_attribute("method", "entry")
        IIDX23ranking.set_attribute("opt", "8208")
        IIDX23ranking.set_attribute("opt2", "0")
        IIDX23ranking.set_attribute("oppid", "51")
        IIDX23ranking.set_attribute("cstage", "4")
        IIDX23ranking.set_attribute("gnum", "967")
        IIDX23ranking.set_attribute("pside", "1")
        IIDX23ranking.set_attribute("clid", "1")
        IIDX23ranking.set_attribute("regist_type", "0" if coursetype == "ir" else "1")
        IIDX23ranking.set_attribute("iidxid", str(iidxid))
        call.add_child(IIDX23ranking)

        # Swap with server
        resp = self.exchange("", call)

        # Verify nodes that cause crashes if they don't exist
        self.assert_path(resp, "response/IIDX23ranking/@anum")
        self.assert_path(resp, "response/IIDX23ranking/@jun")

    def verify(self, cardid: Optional[str]) -> None:
        # Verify boot sequence is okay
        self.verify_services_get(
            expected_services=[
                "pcbtracker",
                "pcbevent",
                "local",
                "message",
                "facility",
                "cardmng",
                "package",
                "posevent",
                "pkglist",
                "dlstatus",
                "eacoin",
                "lobby",
                "ntp",
                "keepalive",
            ]
        )
        paseli_enabled = self.verify_pcbtracker_alive()
        self.verify_package_list()
        self.verify_message_get()
        lid = self.verify_facility_get()
        self.verify_pcbevent_put()
        self.verify_iidx23shop_getname(lid)
        self.verify_iidx23pc_common()
        self.verify_iidx23music_crate()
        self.verify_iidx23shop_getconvention(lid)
        self.verify_iidx23ranking_getranker(lid)
        self.verify_iidx23shop_sentinfo(lid)

        # Verify card registration and profile lookup
        if cardid is not None:
            card = cardid
        else:
            card = self.random_card()
            print(f"Generated random card ID {card} for use.")

        if cardid is None:
            self.verify_cardmng_inquire(card, msg_type="unregistered", paseli_enabled=paseli_enabled)
            ref_id = self.verify_cardmng_getrefid(card)
            if len(ref_id) != 16:
                raise Exception(f"Invalid refid '{ref_id}' returned when registering card")
            if ref_id != self.verify_cardmng_inquire(card, msg_type="new", paseli_enabled=paseli_enabled):
                raise Exception(f"Invalid refid '{ref_id}' returned when querying card")
            self.verify_iidx23pc_reg(ref_id, card, lid)
            self.verify_iidx23pc_get(ref_id, card, lid)
        else:
            print("Skipping new card checks for existing card")
            ref_id = self.verify_cardmng_inquire(card, msg_type="query", paseli_enabled=paseli_enabled)

        # Verify pin handling and return card handling
        self.verify_cardmng_authpass(ref_id, correct=True)
        self.verify_cardmng_authpass(ref_id, correct=False)
        if ref_id != self.verify_cardmng_inquire(card, msg_type="query", paseli_enabled=paseli_enabled):
            raise Exception(f"Invalid refid '{ref_id}' returned when querying card")

        if cardid is None:
            # Verify score handling
            profile = self.verify_iidx23pc_get(ref_id, card, lid)
            if profile["sp_dan"] != -1:
                raise Exception("Somehow has SP DAN ranking on new profile!")
            if profile["dp_dan"] != -1:
                raise Exception("Somehow has DP DAN ranking on new profile!")
            if profile["deller"] != 0:
                raise Exception("Somehow has deller on new profile!")
            if len(profile["ir_data"].keys()) > 0:
                raise Exception("Somehow has internet ranking data on new profile!")
            if len(profile["secret_course_data"].keys()) > 0:
                raise Exception("Somehow has secret course data on new profile!")
            if len(profile["expert_point"].keys()) > 0:
                raise Exception("Somehow has expert point data on new profile!")
            scores = self.verify_iidx23music_getrank(profile["extid"])
            if len(scores.keys()) > 0:
                raise Exception("Somehow have scores on a new profile!")

            for phase in [1, 2]:
                if phase == 1:
                    dummyscores = [
                        # An okay score on a chart
                        {
                            "id": 1000,
                            "chart": 2,
                            "clear_status": 4,
                            "pgnum": 123,
                            "gnum": 123,
                            "mnum": 5,
                        },
                        # A good score on an easier chart of the same song
                        {
                            "id": 1000,
                            "chart": 0,
                            "clear_status": 7,
                            "pgnum": 246,
                            "gnum": 0,
                            "mnum": 0,
                        },
                        # A bad score on a hard chart
                        {
                            "id": 1003,
                            "chart": 2,
                            "clear_status": 1,
                            "pgnum": 10,
                            "gnum": 20,
                            "mnum": 50,
                        },
                        # A terrible score on an easy chart
                        {
                            "id": 1003,
                            "chart": 0,
                            "clear_status": 1,
                            "pgnum": 2,
                            "gnum": 5,
                            "mnum": 75,
                        },
                    ]
                if phase == 2:
                    dummyscores = [
                        # A better score on the same chart
                        {
                            "id": 1000,
                            "chart": 2,
                            "clear_status": 5,
                            "pgnum": 234,
                            "gnum": 234,
                            "mnum": 3,
                        },
                        # A worse score on another same chart
                        {
                            "id": 1000,
                            "chart": 0,
                            "clear_status": 4,
                            "pgnum": 123,
                            "gnum": 123,
                            "mnum": 35,
                            "expected_clear_status": 7,
                            "expected_ex_score": 492,
                            "expected_miss_count": 0,
                        },
                    ]

                for dummyscore in dummyscores:
                    self.verify_iidx23music_reg(profile["extid"], lid, dummyscore)
                self.verify_iidx23pc_visit(profile["extid"], lid)
                self.verify_iidx23pc_save(profile["extid"], card, lid)
                scores = self.verify_iidx23music_getrank(profile["extid"])
                for score in dummyscores:
                    data = scores.get(score["id"], {}).get(score["chart"], None)
                    if data is None:
                        raise Exception(f'Expected to get score back for song {score["id"]} chart {score["chart"]}!')

                    if "expected_ex_score" in score:
                        expected_score = score["expected_ex_score"]
                    else:
                        expected_score = (score["pgnum"] * 2) + score["gnum"]
                    if "expected_clear_status" in score:
                        expected_clear_status = score["expected_clear_status"]
                    else:
                        expected_clear_status = score["clear_status"]
                    if "expected_miss_count" in score:
                        expected_miss_count = score["expected_miss_count"]
                    else:
                        expected_miss_count = score["mnum"]

                    if data["ex_score"] != expected_score:
                        raise Exception(
                            f'Expected a score of \'{expected_score}\' for song \'{score["id"]}\' chart \'{score["chart"]}\' but got score \'{data["ex_score"]}\''
                        )
                    if data["clear_status"] != expected_clear_status:
                        raise Exception(
                            f'Expected a clear status of \'{expected_clear_status}\' for song \'{score["id"]}\' chart \'{score["chart"]}\' but got clear status \'{data["clear_status"]}\''
                        )
                    if data["miss_count"] != expected_miss_count:
                        raise Exception(
                            f'Expected a miss count of \'{expected_miss_count}\' for song \'{score["id"]}\' chart \'{score["chart"]}\' but got miss count \'{data["miss_count"]}\''
                        )

                    # Verify we can fetch our own ghost
                    ex_score, ghost = self.verify_iidx23music_appoint(profile["extid"], score["id"], score["chart"])
                    if ex_score != expected_score:
                        raise Exception(
                            f'Expected a score of \'{expected_score}\' for song \'{score["id"]}\' chart \'{score["chart"]}\' but got score \'{data["ex_score"]}\''
                        )

                    if len(ghost) != 64:
                        raise Exception(f"Wrong ghost length {len(ghost)} for ghost!")
                    for g in ghost:
                        if g != 0x01:
                            raise Exception(
                                f'Got back wrong ghost data for song \'{score["id"]}\' chart \'{score["chart"]}\''
                            )

                # Sleep so we don't end up putting in score history on the same second
                time.sleep(1)

            # Verify that we can save/load expert points
            self.verify_iidx23pc_save(
                profile["extid"],
                card,
                lid,
                {"course_id": 1, "n_point": 0, "h_point": 500, "a_point": 0},
            )
            profile = self.verify_iidx23pc_get(ref_id, card, lid)
            if sorted(profile["expert_point"].keys()) != [1]:
                raise Exception("Got back wrong number of expert course points!")
            if profile["expert_point"][1] != {
                "n_point": 0,
                "h_point": 500,
                "a_point": 0,
            }:
                raise Exception("Got back wrong expert points after saving!")
            self.verify_iidx23pc_save(
                profile["extid"],
                card,
                lid,
                {"course_id": 1, "n_point": 0, "h_point": 1000, "a_point": 0},
            )
            profile = self.verify_iidx23pc_get(ref_id, card, lid)
            if sorted(profile["expert_point"].keys()) != [1]:
                raise Exception("Got back wrong number of expert course points!")
            if profile["expert_point"][1] != {
                "n_point": 0,
                "h_point": 1000,
                "a_point": 0,
            }:
                raise Exception("Got back wrong expert points after saving!")
            self.verify_iidx23pc_save(
                profile["extid"],
                card,
                lid,
                {"course_id": 2, "n_point": 0, "h_point": 0, "a_point": 500},
            )
            profile = self.verify_iidx23pc_get(ref_id, card, lid)
            if sorted(profile["expert_point"].keys()) != [1, 2]:
                raise Exception("Got back wrong number of expert course points!")
            if profile["expert_point"][1] != {
                "n_point": 0,
                "h_point": 1000,
                "a_point": 0,
            }:
                raise Exception("Got back wrong expert points after saving!")
            if profile["expert_point"][2] != {
                "n_point": 0,
                "h_point": 0,
                "a_point": 500,
            }:
                raise Exception("Got back wrong expert points after saving!")

            # Verify that a player without a card can play
            self.verify_iidx23pc_playstart()
            self.verify_iidx23music_play(
                {
                    "id": 1000,
                    "chart": 2,
                    "clear_status": 4,
                    "pgnum": 123,
                    "gnum": 123,
                }
            )
            self.verify_iidx23pc_playend()

            # Verify shop name change setting
            self.verify_iidx23shop_savename(lid, "newname1")
            newname = self.verify_iidx23shop_getname(lid)
            if newname != "newname1":
                raise Exception("Invalid shop name returned after change!")
            self.verify_iidx23shop_savename(lid, "newname2")
            newname = self.verify_iidx23shop_getname(lid)
            if newname != "newname2":
                raise Exception("Invalid shop name returned after change!")

            # Verify beginner score saving
            self.verify_iidx23music_breg(
                profile["extid"],
                {
                    "id": 1000,
                    "clear_status": 4,
                    "pgnum": 123,
                    "gnum": 123,
                },
            )
            scores = self.verify_iidx23music_getrank(profile["extid"])
            if 1000 not in scores:
                raise Exception(f"Didn't get expected scores back for song {1000} beginner chart!")
            if 6 not in scores[1000]:
                raise Exception(f"Didn't get beginner score back for song {1000}!")
            if scores[1000][6] != {"clear_status": 4, "ex_score": -1, "miss_count": -1}:
                raise Exception("Didn't get correct status back from beginner save!")

            # Verify DAN score saving and loading
            self.verify_iidx23grade_raised(profile["extid"], newname, "sp")
            self.verify_iidx23grade_raised(profile["extid"], newname, "dp")
            profile = self.verify_iidx23pc_get(ref_id, card, lid)
            if profile["sp_dan"] != 5:
                raise Exception("Got wrong DAN score back for SP!")
            if profile["dp_dan"] != 5:
                raise Exception("Got wrong DAN score back for DP!")

            # Verify secret course and internet ranking course saving
            self.verify_iidx23ranking_entry(profile["extid"], newname, "ir")
            self.verify_iidx23ranking_entry(profile["extid"], newname, "secret")
            profile = self.verify_iidx23pc_get(ref_id, card, lid)
            for ptype in ["ir_data", "secret_course_data"]:
                if profile[ptype] != {2: {1: {"clear_status": 4, "pgnum": 1771, "gnum": 967}}}:
                    raise Exception(f"Invalid data {profile[ptype]} returned on profile load for {ptype}!")
        else:
            print("Skipping score checks for existing card")

        # Verify paseli handling
        if paseli_enabled:
            print("PASELI enabled for this PCBID, executing PASELI checks")
        else:
            print("PASELI disabled for this PCBID, skipping PASELI checks")
            return

        sessid, balance = self.verify_eacoin_checkin(card)
        if balance == 0:
            print("Skipping PASELI consume check because card has 0 balance")
        else:
            self.verify_eacoin_consume(sessid, balance, random.randint(0, balance))
        self.verify_eacoin_checkout(sessid)
