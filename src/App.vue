<template>
  <el-container class="app-container">
    <el-header class="frens-header">Frens rarity checker</el-header>
    <el-main>
      <el-row class="row-bg" justify="center">
        <el-col :sm="24" :md="12" :lg="8" :xl="6">
          <el-form
            @submit.prevent
            :model="checkForm"
            ref="formRef"
            label-width="120px"
          >
            <el-form-item
              label="Frens id"
              prop="frensId"
              :rules="[
                { required: true, message: 'frens id is required' },
                { type: 'number', message: 'frens id must be a number' },
              ]"
            >
              <el-input
                v-model.number="checkForm.frensId"
                type="text"
                autocomplete="off"
                v-on:keyup.enter="submitForm(formRef)"
              />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm(formRef)"
                >Check estimated prices</el-button
              >
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <el-row v-if="fren" class="row-bg" justify="center">
        <el-col :sm="24" :md="12" :lg="8" :xl="6">
          <el-descriptions
            title="Estimated prices based on different algorithms"
            direction="horizontal"
            :column="1"
            size="large"
            border
          >
            <el-descriptions-item label="Fren id">
              {{ fren.id }}
            </el-descriptions-item>
            <el-descriptions-item label="Rarity score">
              {{ Math.round(fren.rarity_score) }}
            </el-descriptions-item>
            <el-descriptions-item label="KRV">
              <template v-slot:label>
                <el-popover
                  placement="top-start"
                  title="KRV"
                  :width="500"
                  trigger="hover"
                >
                  <template #reference>
                    KRV ℹ️
                  </template>
                  The Kryoten Rarity Valuation. <br>
                  This is an algorithm designed by Kryoten to come up with a PRE-Market Valuation based on solely rarity score. This is the simplest metric and as valued by Kryoten, should be the lowest expected price to trade a Fren for given there are no official market values or floor prices yet.
                </el-popover>
              </template>
              {{ Math.round(fren.krv) }} Stars
            </el-descriptions-item>
            <el-descriptions-item label="KARV">
              <template v-slot:label>
                <el-popover
                  placement="top-start"
                  title="KARV"
                  :width="500"
                  trigger="hover"
                >
                  <template #reference>
                    KARV ℹ️
                  </template>
                  The Kryoten Accelerated Rarity Valuation.<br>
                  This is the companion algorithm to give a more speculative price based on other NFT projects, also accounting for value and growth in floor prices, with similar supply. This number is a range speculating todays KARV, and a future price based on a time span of 2 years.
                </el-popover>
              </template>
              {{ Math.round(fren.karv_present) }} Stars (today) -
              {{ Math.round(fren.karv_future) }} Stars (2 years from now)
            </el-descriptions-item>
            <el-descriptions-item label="KHRV">
              <template v-slot:label>
                <el-popover
                  placement="top-start"
                  title="KHRV"
                  :width="500"
                  trigger="hover"
                >
                  <template #reference>
                    KHRV ℹ️
                  </template>
                  The Kryoten Hubble Rarity Valuation.<br>
                  This is a similar algorithm to KRV, however this is accounting for rarity scores given by hubble.tools, given they have a different scoring system. This dilutes the KRV rating significantly and more so is a companion for the KHARV algorithm.
                </el-popover>
              </template>
              {{ Math.round(fren.khrv) }}
            </el-descriptions-item>
            <el-descriptions-item label="KHARV">
              <template v-slot:label>
                <el-popover
                  placement="top-start"
                  title="KHARV"
                  :width="500"
                  trigger="hover"
                >
                  <template #reference>
                    KHARV ℹ️
                  </template>
                  The Kryoten Hubble Accelerated Valuation.<br>
                  This algorithm has had all factors up to this point accounted for and could be the most accurate for fair PRE-Market valuations. Similar to KARV, is also a range speculating todays KHARV, and a future price based on a time span of 2 years.
                </el-popover>
              </template>
              {{ Math.round(fren.kharv_present) }} Stars (today) -
              {{ Math.round(fren.kharv_future) }} Stars (2 years from
              now)</el-descriptions-item
            >
          </el-descriptions>
          <el-image class="fren-image" :src="fren.img" />
        </el-col>
      </el-row>
    </el-main>
    <el-footer class="frens-footer">
      ❤️ Built with love ❤️<br />
      Starsbook donation address:
      juno1vrgrym3nnazzvkgwzxp7tvq9es0awv00zsz9fg7e9lp837kul62q6qds2s
    </el-footer>
  </el-container>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import type { FormInstance } from "element-plus";
import { InfoFilled } from "@element-plus/icons-vue";
import nftRarity from "@/assets/values.json"; // TODO: transform into map instead of array for easier access

const formRef = ref<FormInstance>();

const checkForm = reactive({
  frensId: "",
});

const fren = ref<any>(undefined);

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      check(checkForm.frensId);
    } else {
      return false;
    }
  });
};

function check(frensId: string) {
  const frenFound = (
    nftRarity as unknown as {
      [key: string]: {
        id: string | undefined;
        img: string | undefined;
        rarity_score: number;
        krv: number;
        karv_present: number;
        karv_future: number;
        khrv: number;
        kharv_present: number;
        kharv_future: number;
      };
    }
  )[frensId];

  if (typeof frenFound === "undefined") {
    alert("Fren not found");
    return;
  }

  frenFound.id = frensId;
  frenFound.img = `https://stargaze.mypinata.cloud/ipfs/bafybeiaip3vwwhhgerw6gcs66clj4onubkdadquqzzpzrftvuyhgnzojse/images/${frensId}.jpg?img-width=600&img-fit=scale-down&img-anim=false&img-format=auto`;

  fren.value = frenFound;
}
</script>

<style>
@import "assets/base.css";

.app-container {
  height: 100%;
}

.frens-header {
  text-align: center;
  font-size: 32px;
}

.frens-footer {
  margin-top: auto;
  text-align: center;
  overflow-wrap: anywhere;
}

.fren-image {
  margin-top: 25px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>
