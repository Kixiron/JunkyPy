# JunkyPy

## A C# pseudocode generator written in Python

-----

## How to use

JunkyPy reads through all `.cs` files in a directory until it encounters one of the following comments:

```cs
/* SKIP FILE */
```

Skips file

-----

```cs
/* INSERT JUNK FUNCTION */
```

Creates procedurally generated functions with `if` and `for` statements

-----

```cs
/* INSERT JUNK CLASS */
```

Creates a procedurally generated class with `enums`, functions and private variables

-----

```cs
/* INSERT JUNK PRIVATE VARIABLES */
```

Creates procedurally generated private variables

-----

```cs
/* INSERT JUNK IMPORTS */
```

Inserts multiple imports from the `System` namespace

-----

## Example

Code goes from this

```cs
using System;

/* INSERT JUNK IMPORTS */

public class ExampleNamespace
{
    /* INSERT JUNK PRIVATE VARIABLES */

    class ExampleClass
    {
        public void ExampleFunction()
        {
            if (true)
            {
                Console.WriteLine("True!");
            }
        }

        /* INSERT JUNK FUNCTION */
    }

    /* INSERT JUNK CLASS */
}
```

To this:

```cs
/* This file has been junkified by JunkyPy */
using System;

/* START JUNK */
using System.Globalization;
/* END JUNK IMPORTS */

public class ExampleNamespace
{
    /* START JUNK */
    private static UIntPtr luRyodDpSpIcMWUSmBqkSjBSfwJF;
    private static IntPtr sTRgVS;
    /* END JUNK PRIVATE VARS */


    class ExampleClass
    {
        public void ExampleFunction()
        {
            if (true)
            {
                Console.WriteLine("True!");
            }
        }

        /* START JUNK */
        private async void QnJLzELvtNZmyBlNmJlfFBzzDnIWhqetsl_func()
        {
            if ((2636721179645438611 < 2621362743931512144) || (16205603638910925956 != 7533604575105465452) || (18411896134389824287 != 10140543202383425322))
            {
                short CVccrFuOXiFXcFEHRteasaHsy = 12635;
                bool xRrYPIjUrcZIJlBmknzVtkYokzSorqZ = null;
                for (var cSaAFPMxBMfjRES = 0; cSaAFPMxBMfjRES <= -1206790543510731794; cSaAFPMxBMfjRES++)
                {
                    if ((-1043074240063478766 < 6981484217441753527) || (-8569970858416433640 < 9527803358482453187))
                    {
                        ulong QJcQodtmHVWFUtbclZFWrJCi = -4875673774156661270;
                        bool uRYvAapQMVgcxuZppgiIAFBvbpofVVyMosmKdCGUCWZN = false;
                        bool EvGsJdPWdLZaIfeByMMwuhZe = true;
                        short UvTsy = -31579;
                    }
                }
                for (var kfgwTbzZRRZsdfvDgbFfmKiFNa = 0; kfgwTbzZRRZsdfvDgbFfmKiFNa > 322824997620390145; kfgwTbzZRRZsdfvDgbFfmKiFNa++)
                {
                    if ((-1089895133908382931 >= 628069318074094535) || (1175103492025601771 <= 10375135292228046574) || (17632757567911898478 < 15176941562663994558) || (5223218071743807073 != 14970743583964020595))
                    {
                        long zouyLvkThrYSvUwafHoSyNBjIFCC = -8652498269924522568;
                        short vfFgJAhM = -30229;
                        int yxwARNhzoBFBhHHVXSXkMfPKyBGpWS = 1887007619;
                        short CNbLJLuZaHraslcVjHnawyzrcAeoRtehRucNOBpAySA = -6937;
                    }
                }
            }
            for (var WWaCkakNLUwCGDlZuzHOdaDcMgu = 0; WWaCkakNLUwCGDlZuzHOdaDcMgu >= -16212286269800627045; WWaCkakNLUwCGDlZuzHOdaDcMgu++)
            {
                if ((-6919597392123082139 < 15090068184238089411) || (-10089283706234481759 != 12212025749806265695) || (17222126986293722279 > -1416244147351037569))
                {
                    ulong kKOjzoKXxecEAnmURenjCWuuhySxWurHHwOQiF = 3453291266407184432;
                    long vxdouNTXGsYIWaaSdIqC = -4165811910021754922;
                    for (var HsWykYzXHlSuKzmaRKcbFDQtNzArpncwusmgNb = 0; HsWykYzXHlSuKzmaRKcbFDQtNzArpncwusmgNb <= -16001848720930805078; HsWykYzXHlSuKzmaRKcbFDQtNzArpncwusmgNb++)
                    {
                        if ((4408005764297006627 >= -5947608402354862372) && (8504012865900711488 == 7693518005434874133) && (-16580154253276388437 != -950781365747492135) && (-12235661240626272487 < 2476151552684105152))
                        {
                            byte pFhtwwjBjqcvZHGaeqhmzgbLmVgEgxveUdVDQGmhBQcEhcK = 34;
                            int vYIFCSAFIVRFJPCwoKQiopqLwNDbJAViRwmRHqyUiOdvCDz = 834294542;
                            bool MeasBTZTHINRAGmtEDWPeVktRwneXBfEvCgb = null;
                            short PUqFXWTxSCHvSUlfGMirKmugkhdYou = 29160;
                        }
                    }
                }
                if ((7954890857290270561 < 1599790174587232254) || (-11762515164378576428 != -9786771692505641081))
                {
                    int cYfxKmKeEJCBQjCphVsnQQJxSxygbCMUiUCWysTgWboWwPIMC = -1571625379;
                    short SUAbpTWwIreJUQhrOqACUvLYhhloPGBbxwYLxf = -5751;
                    byte JGyEIDENIsdpgLpUErqKxiGRQFQRLnBfgirgvPNnpFRbNNJoA = 165;
                    int fURbUmCOFZyW = -1181830960;
                }
            }
            for (var OoHtO = 0; OoHtO < -17412366981778165602; OoHtO++)
            {
                if ((1743032239118174583 > 12069659904373237396) || (9123504734697695710 >= 10872729919171089084) || (-11842161852662797200 < -4625550638024796205))
                {
                    bool umcPVpjmngHjhiEWwhStNqAbZyZEJnRFxYOFjxusZKrma = null;
                    ulong JbriYFweer = -1018602705366327830;
                    long jLEUsNLnAzaRNWHyOuTYmoRCOSuIW = 5449128755999468006;
                    uint cvxtmrzKUqlFTGtIAiRTHOtnlHcJMZmUQ = -4166932722;
                    for (var XMpZYNIvBuOCbphRXNBHBKbxZq = 0; XMpZYNIvBuOCbphRXNBHBKbxZq > -5490775998312295932; XMpZYNIvBuOCbphRXNBHBKbxZq++)
                    {
                        if ((-14248538354096860123 < 9444178403871711344))
                        {
                            ulong otBFAuAQvlMLtOuKSDFAXoRxLogDXzUHBtKeoqbyBumhuuqura = 4605315501410067493;
                            byte qRePLWKWA = 5;
                            ulong aEzwmJGUumLbMprfoXoPwRKXMWudsIpVGIqPh = 13998825593212615171;
                        }
                        if ((-9345453973456846212 >= -13286097231176197397) && (-12373139532493084707 == -13396598666284432418))
                        {
                            ulong DaQWhHTMduwccwDmDriDcqWNHsy = 16615623172362143231;
                        }
                    }
                    for (var OvgJSrpLJfzQMAwVETmhijecRHklaADKzVPCsNdvzerPY = 0; OvgJSrpLJfzQMAwVETmhijecRHklaADKzVPCsNdvzerPY > -15322588055841544193; OvgJSrpLJfzQMAwVETmhijecRHklaADKzVPCsNdvzerPY++)
                    {
                        if ((7359745623872903483 < -1666606194407828243) || (-17682670804317166121 != 9447849976334607466) || (-5419062513679883596 == -5570670855856016410))
                        {
                            uint UGmQULSXOXbfdSgRHXOgoPHxdRaxehuOURDYpJRHH = 497872999;
                            short SeIBRJdjnlhRPjhxXeeiYnuOENnUpsb = 4219;
                            int OCMtqj = -1996713044;
                        }
                        if ((3464409343943789682 < -3919348600519521224) && (-6389519503912057593 < 14896437884209854242) && (9732716937546633979 < -7435425326260887935) && (8595135958023347764 <= -2935210272216263061))
                        {
                            byte FTnfdOvlFgtgrw = 253;
                            uint PTQLktxSQcGrvrNnrkBsLCLDHqiVhbAeUFSvc = 1835153552;
                            byte eBryPfSVbYVwpejEOog = 200;
                            int DfeoyQiMUZWIcdeNrMbrQqAYbjfyvugnGnGltbWM = -820456106;
                        }
                    }
                }
                if ((9077933556263668671 < 14243646345489560723))
                {
                    byte UgcMgCcLSiKPAvptKMopl = 184;
                }
            }
            for (var KSNxcVGmATvirTAcLVgRZKrWuPdizKtJdbdRujotczk = 0; KSNxcVGmATvirTAcLVgRZKrWuPdizKtJdbdRujotczk > 11098522810486483256; KSNxcVGmATvirTAcLVgRZKrWuPdizKtJdbdRujotczk++)
            {
                if ((2749312809062941136 == 2883942039222697537) && (-875070827858488809 < 10465360678029744145) && (3507133963010490808 <= -8925244393538904899))
                {
                    uint iJRazdlzRrPoiAkkQCfLmNWwrjGG = -1835283003;
                    byte KYMWTZBjWKYsBveeiEyMWAXbAQEizBxPWcwqQWsV = 199;
                    uint weOqotrWmkuosMfeJwmcRbBpnVTFAXEokqO = -754769837;
                    ulong GbzulgrumdV = 14318010043973649069;
                    for (var modZkgB = 0; modZkgB > 8011310102385709877; modZkgB++)
                    {
                        if ((-3667034918437950275 <= -4564392019352295550) || (9973346189934226413 == -14804918292169268212))
                        {
                            long KAvGagATphzOEvEsfOjgBcOMpXwJUHAyFNRNYgwMtStc = 2548764749975950278;
                        }
                        if ((16606958176361762182 > -17338412981857592390) || (6307171350144145208 <= -2619791587241506350) || (11764300122996983768 != 16183713425386715702) || (12479462502710540049 >= -5310373873870479734))
                        {
                            int LxciqOdFuPzGgFFmWNMYatSUbyLWuCRoQxvLn = -821510303;
                            bool UVDYvHmnAC = true;
                            bool fASGHIZVuaNxsvfUgWhOrcePWrvBwbnqzUWKgEmrr = false;
                        }
                    }
                }
            }
        }
        /* END JUNK FUNCTION */
    }

    /* START JUNK */
    private class ALabwlUf_class
    {
        private static UIntPtr[] dzokLsxWWNYTk;
        private static char zMOeGRdBsYdSNGqqkBnfT;
        [Flags]
        private enum xwqHKMhuDQRHQZmpMgvgawNMSRMNNIttuNEaEl_enum : long
        {
            bQyabPhUZ = 1847894798553445369,
            jXqZKWPuUHWRlkxyR = 191575365050791400,
            RaLTMUsyDzfknzxiJTrkXLSWbDMueBLBCYewarZT = -5510450283592394467,
        }
        [Flags]
        private enum PAwcgDrcGUZBgcRSCAwhbTTnYkIjOwSoHPTIIOKPaTXVyabHgL_enum : byte
        {
            afRZAGPeJBnooAcFQZw = 31,
            uMlTSYdADDPmsZnROhuuauXRikeoxeicYrBGYbPKNFWtsXkegv = 135,
            wGvHtuBBetaNgHhsrlQeMARdUmWG = 193,
        }
        private async void xTjdvPfVuppUkDjVfAGEGFtWfMjevXIUjWnoncVL_func()
        {
            if ((-18321370038937270169 == -9178995404173922845) && (10396958383423580741 == -4202908588808517103))
            {
                long SPtflDuqjuZbmGydtwkeNjEFMrH = 8709256852230902827;
                int uPgPHumryxAKjcUDlOEClvrgSjDjlhUBidRBpczNbmkkPTadBk = 1510632723;
            }
            if ((-17991003487609872917 >= 15829128375596881539) || (14277402890469746014 < 13443734566093230522))
            {
                short ybmIkrAQsgoDyKwVNQAmBmiDWP = -271;
                bool EhMYJjfggDqcFNxOeUQsiVosHvzVUnFKkNcVtNJbGyA = false;
                short iJDFtQHilbRzIgSnisugQJkwVVK = -22601;
                for (var KTimUNXcapfQMVZbTOdlXwrGMyzB = 0; KTimUNXcapfQMVZbTOdlXwrGMyzB > 9158672165719675299; KTimUNXcapfQMVZbTOdlXwrGMyzB++)
                {
                    if ((-14791671847048449824 > -330966700988769317))
                    {
                        uint CQGYhSUTSaqQdGfJUr = 3511684546;
                        byte khKyoBsH = 251;
                        bool oUOZsawhZXehwjWFMCshdMbDdrBVKwEasMoWXReoCiMovzkNRn = true;
                        ulong sYeKCZQJZQUHMEfSYvIiFxFkdA = 8703181537440854401;
                    }
                }
            }
            if ((1689602772993643019 > -8345841009576247785))
            {
                uint mBkuALusVfmsnEvFpfXpFmDQNCgsjtoNPoefGpEC = -2159414810;
                uint fZwmmVFtkjbeGbjnvDV = -386857831;
                int sfbcMYcNsEb = -1529892168;
                bool lpVMLBUxqL = null;
                for (var XIhXRiMOw = 0; XIhXRiMOw <= -9441933342936724318; XIhXRiMOw++)
                {
                    if ((-2397868941297921450 <= 14352232794838451518))
                    {
                        byte tANSnIu = 243;
                    }
                    if ((14769177969782390417 >= 4883420822436722458) || (16995592000256374355 != -3777519926572981667))
                    {
                        short KjxThLUpIaHKvqf = -12183;
                        ulong RcbCUMJKtDGGSLrGHMHBwPWSalATVlCwqINSEU = 15136774554013385440;
                        short BCjjQ = -31782;
                        long oxbrP = -4245361335682020088;
                    }
                }
            }
            for (var KBRMOKTmsm = 0; KBRMOKTmsm < 14912214656553787928; KBRMOKTmsm++)
            {
                if ((-3729782852445673840 <= 7425432108026685885) || (-8353733809720443742 != -15187535516236158735) || (3022248518177466361 != -3203232838543137111))
                {
                    uint oqSFJERxapfi = -2255169661;
                    int pOWuDUoaLD = -1280969552;
                    int VJmZW = -1510832004;
                    for (var pfBeWbxkSRnBaERdETsVJBnx = 0; pfBeWbxkSRnBaERdETsVJBnx < 17340405233701954783; pfBeWbxkSRnBaERdETsVJBnx++)
                    {
                        if ((6575256191751866716 >= -15710771835830067195) && (-2619293001758928581 >= -12609451013316774364))
                        {
                            long nwYKEglFabYIptPiwjJDpyVrDXnouIVvdXetFZxIiKjBSkd = 4990587260298032945;
                            ulong gbaHCwTFwMPLnKnyeyfkyHmSvPnRsKflDTwYI = 5618758141796508026;
                            ulong ySkzYQkExEcQVZBhmhnEoIfZHodxbiDzjDYJJYWcOpdQrb = 641074857979634862;
                        }
                        if ((-17247371899591124738 <= 17443789728066564153) && (13107463901887776899 >= -10382870708189123933) && (2341099029077827109 < -5292669608709434324) && (-4669333632192139806 <= -13467771317512940363))
                        {
                            uint CkjnceCBoIexXzjrkrqZpxCglXCo = -94709952;
                            bool aCUOelhHWe = null;
                            byte zkBfnWIRsIgNtbJOfUrtsPVWP = 64;
                        }
                    }
                    for (var tIlCkVFtoYZvcw = 0; tIlCkVFtoYZvcw < 13140759737880595343; tIlCkVFtoYZvcw++)
                    {
                        if ((-16175311463479868905 < -10046180684600828470) || (-3588461252775892646 > -14568899728505740493))
                        {
                            long vWHiukkqtrmBBluafjVxgqlbmTeZZjuEty = -3966773579566981021;
                            long ylvjjpA = 4881949249656787740;
                            int oayufrHbGBnatHhfKDBoqWfNDuAt = -174025598;
                            ulong ttxGEuplOwnjtMljnRNsyanoSsddEhC = 15594657686941667256;
                        }
                        if ((-4669363787126895511 < 9052106100985058444) && (183401808769885077 == -8794916300946997519))
                        {
                            bool rwxxlzJmUwjygZUXQCsIorPawauT = false;
                            byte oypghEmLYGhODDUZGDknKpK = 29;
                        }
                    }
                }
                if ((-3833865152015173757 == 7983097217532678708))
                {
                    short GtZeumkFcAxJekFDUnNkwSiw = -12126;
                    byte TLOmVWsIXibyMsvYYeztpSRrYFkODuEgCrLbjkgbEYPGfVKDzc = 98;
                    bool hkTiWFLfTfxLZoTCGYaAcpHpfohKNCuICipaNoDHEtBJGgfG = true;
                    for (var SiCOate = 0; SiCOate >= -5221205358884541588; SiCOate++)
                    {
                        if ((-18248484163567162208 < 17311094614900542492))
                        {
                            long VZuxILqhZrUiUhKlzQdtoFMGYWltdUXuyYOxfGnBDGkCJUFRn = 2636298405996377740;
                            int nkrwkyvEpvjT = 222832641;
                        }
                        if ((-4568095759498157293 > -582544684675893499) && (8543840801604099179 == 16584410446073323443) && (12934585563969024886 > 1191099250500203090))
                        {
                            bool OqEDivFLuySsbroMzW = false;
                            int cMRKVNulAeUdgSCzZQBFsHSsJswHs = 1780545273;
                            int FnBMLyNpNVijjzWzu = -996901622;
                            bool MWHQJLJmXNMQVOt = null;
                        }
                    }
                    for (var zCBmYZWQicZJwHuULSEcwpbUSS = 0; zCBmYZWQicZJwHuULSEcwpbUSS < -2091970814622747108; zCBmYZWQicZJwHuULSEcwpbUSS++)
                    {
                        if ((-1107887517165068441 < -16773299387817118709))
                        {
                            ulong iJZHMrFkrmFdlpRPtQFSCQHzLRyJedRpxmQRiO = 4446249873439430824;
                            long mgTrfKgiiFGprdPIuEGsakEtVMPygMnSkyYjhwaOmc = -7880738180145686985;
                        }
                        if ((-6146293808271821357 != -15146195903357550938) && (-6623918886330758487 <= -10913185680905225028) && (10796388736367469624 < -18298051408415659250) && (-16674261940691260822 != -17164876752611561277))
                        {
                            long MENmUxjjojkoQbmaPFuZhTRmqOHRoFJwLgdM = -8579626300848103405;
                            long jyhJZqfsqPpdqHmmiCDXLNEVxHJyiOtNLcRJLeqikXKDijok = 9025285264797872505;
                            uint nKkVCkhEDiIxT = -2865051478;
                        }
                    }
                }
            }
            for (var yPIVlusJyimeDxZ = 0; yPIVlusJyimeDxZ >= -8499222660059266949; yPIVlusJyimeDxZ++)
            {
                if ((7347597032059604113 > 9349756288237932979) && (15118292780103594910 >= 7921956761920954811))
                {
                    bool wiJaAumVgaaftRtMXUN = true;
                    ulong LuFdHVbSIilvqryuKfZsicUMNrpqrIuYI = 1859734312345159272;
                    uint rATlqyKRsPynnReDGTBiDFwwvAqBjpTfKHXPiRfSVbVhlA = 1836276274;
                    for (var RRhiyYnDYWbnmIOhxmJhSWQjiOoLwtYGqaqksKgDnSQt = 0; RRhiyYnDYWbnmIOhxmJhSWQjiOoLwtYGqaqksKgDnSQt > 9064425290085460920; RRhiyYnDYWbnmIOhxmJhSWQjiOoLwtYGqaqksKgDnSQt++)
                    {
                        if ((-8862368592469706651 < -9247221433968167401) && (3588197467274206926 > -1211736450279002663))
                        {
                            byte ysCkgULlUystkwCpeYJAyzZTirfZye = 183;
                        }
                    }
                }
                if ((11641892993179943362 > -4367025351114794573))
                {
                    long eJYZdYKDrHkeCuGgyQYMfzoJxskWGHoTbsuOb = -110185533811226055;
                    bool OWfzGgSJRBOuwlrCuXf = true;
                    ulong jBkbtnIjLAHbuwCGGjMAxFGN = 1022897237966614125;
                    for (var jVUmVceBxHMzGFVENlDuGmIhKhpPyYaCCOwDbpyyyhDXkagMBr = 0; jVUmVceBxHMzGFVENlDuGmIhKhpPyYaCCOwDbpyyyhDXkagMBr < 17353685629370465123; jVUmVceBxHMzGFVENlDuGmIhKhpPyYaCCOwDbpyyyhDXkagMBr++)
                    {
                        if ((13443839113936440470 <= -14938376179596820517) && (-10033776425948376429 == 6614120933035915332) && (-17416782234898429632 > -8794258090847857485))
                        {
                            uint feZXmnUIeXm = -1796797352;
                        }
                    }
                }
                if ((4134630675829337718 != -14593170455085424757))
                {
                    long AkltZyHusvkeaoyTKHOWyE = -7827641302641254734;
                    bool prvsTxpYslfdwEZFebMALCLAGalbDk = true;
                    uint zOotRJABmgGfmUvmxoSrCLhhbRtyrvskhozvPT = 1777034344;
                    short IdqgfDiuVPjSLXWLDudAMv = -3158;
                }
            }
        }
    }
    /* END JUNK CLASS */
}
```

In short, JunkyPy is quite powerful, so use it sparingly!  
If run again, JunkyPy will un-junk your code for easy access.  
Remember that only `.cs` files *directly* inside of the specified directory will be junkified
